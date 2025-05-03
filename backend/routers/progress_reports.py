from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.child_profile import ChildProfile
from ..models.writing_session import WritingSession
from ..models.writing_assessment import WritingAssessment
from ..schemas.progress_report import ProgressReportResponse
from pydantic import BaseModel, ConfigDict
from datetime import datetime


router = APIRouter(prefix="/api/progress-reports", tags=["progress-reports"])


class ProgressReportBase(BaseModel):
    child_id: int
    overall_progress: dict
    strength_areas: list
    improvement_areas: list
    milestones: list
    recommendations: list


class ProgressReportCreate(ProgressReportBase):
    pass


class ProgressReportUpdate(ProgressReportBase):
    pass


class ProgressReportResponse(ProgressReportBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


@router.post("/", response_model=ProgressReportResponse)
async def create_progress_report(
    report: ProgressReportCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new progress report.
    
    Args:
        report: Progress report data
        db: Database session
    
    Returns:
        Created progress report
    """
    # Verify child exists
    child = db.query(ChildProfile).filter(ChildProfile.id == report.child_id).first()
    if child is None:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    db_report = ProgressReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


@router.get("/", response_model=List[ProgressReportResponse])
async def get_progress_reports(
    child_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get a list of progress reports.
    
    Args:
        child_id: Optional filter by child ID
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session
    
    Returns:
        List of progress reports
    """
    query = db.query(ProgressReport)
    if child_id:
        query = query.filter(ProgressReport.child_id == child_id)
    reports = query.offset(skip).limit(limit).all()
    return reports


@router.get("/{report_id}", response_model=ProgressReportResponse)
async def get_progress_report(
    report_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific progress report by ID.
    
    Args:
        report_id: ID of the progress report
        db: Database session
    
    Returns:
        Progress report
    """
    report = db.query(ProgressReport).filter(ProgressReport.id == report_id).first()
    if report is None:
        raise HTTPException(status_code=404, detail="Progress report not found")
    return report


@router.put("/{report_id}", response_model=ProgressReportResponse)
async def update_progress_report(
    report_id: int,
    report: ProgressReportUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a progress report.
    
    Args:
        report_id: ID of the progress report
        report: Updated report data
        db: Database session
    
    Returns:
        Updated progress report
    """
    db_report = db.query(ProgressReport).filter(ProgressReport.id == report_id).first()
    if db_report is None:
        raise HTTPException(status_code=404, detail="Progress report not found")
    
    for key, value in report.dict().items():
        setattr(db_report, key, value)
    
    db.commit()
    db.refresh(db_report)
    return db_report


@router.delete("/{report_id}")
async def delete_progress_report(
    report_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a progress report.
    
    Args:
        report_id: ID of the progress report
        db: Database session
    
    Returns:
        Success message
    """
    db_report = db.query(ProgressReport).filter(ProgressReport.id == report_id).first()
    if db_report is None:
        raise HTTPException(status_code=404, detail="Progress report not found")
    
    db.delete(db_report)
    db.commit()
    return {"message": "Progress report deleted successfully"}


@router.get("/{child_id}", response_model=ProgressReportResponse)
def get_child_progress(child_id: int, db: Session = Depends(get_db)):
    """Get progress report for a specific child."""
    # Verify child exists
    child = db.query(ChildProfile).filter(ChildProfile.id == child_id).first()
    if not child:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    # Get all writing sessions for the child
    writing_sessions = db.query(WritingSession).filter(WritingSession.child_id == child_id).all()
    
    # Get all assessments for these sessions
    session_ids = [session.id for session in writing_sessions]
    assessments = db.query(WritingAssessment).filter(WritingAssessment.writing_session_id.in_(session_ids)).all()
    
    # Calculate average score
    total_score = sum(assessment.score for assessment in assessments) if assessments else 0
    average_score = total_score / len(assessments) if assessments else 0
    
    # Compile areas for improvement and strengths
    areas_for_improvement = []
    strengths = []
    for assessment in assessments:
        if assessment.areas_for_improvement:
            areas_for_improvement.extend(assessment.areas_for_improvement.split(","))
        if assessment.strengths:
            strengths.extend(assessment.strengths.split(","))
    
    # Remove duplicates and get top 5
    areas_for_improvement = list(set(areas_for_improvement))[:5]
    strengths = list(set(strengths))[:5]
    
    return {
        "child_id": child_id,
        "total_sessions": len(writing_sessions),
        "average_score": average_score,
        "areas_for_improvement": areas_for_improvement,
        "strengths": strengths
    } 