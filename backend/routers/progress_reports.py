from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import ProgressReport, ChildProfile
from pydantic import BaseModel
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

    class Config:
        orm_mode = True


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