from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import WritingSession, WritingAssessment, ChildProfile
from pydantic import BaseModel
from datetime import datetime


router = APIRouter(prefix="/api/writing-sessions", tags=["writing-sessions"])


class WritingSessionBase(BaseModel):
    child_id: int
    topic: str
    writing_mode: str
    content: str
    word_count: int
    duration: int


class WritingSessionCreate(WritingSessionBase):
    pass


class WritingSessionUpdate(WritingSessionBase):
    pass


class WritingSessionResponse(WritingSessionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class WritingAssessmentBase(BaseModel):
    grade_level: str
    grammar_score: str
    structure_score: str
    vocabulary_score: str
    feedback: str
    strengths: list
    areas_for_improvement: list


class WritingAssessmentCreate(WritingAssessmentBase):
    pass


class WritingAssessmentResponse(WritingAssessmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


@router.post("/", response_model=WritingSessionResponse)
async def create_writing_session(
    session: WritingSessionCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new writing session.
    
    Args:
        session: Writing session data
        db: Database session
    
    Returns:
        Created writing session
    """
    # Verify child exists
    child = db.query(ChildProfile).filter(ChildProfile.id == session.child_id).first()
    if child is None:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    db_session = WritingSession(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


@router.get("/", response_model=List[WritingSessionResponse])
async def get_writing_sessions(
    child_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get a list of writing sessions.
    
    Args:
        child_id: Optional filter by child ID
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session
    
    Returns:
        List of writing sessions
    """
    query = db.query(WritingSession)
    if child_id:
        query = query.filter(WritingSession.child_id == child_id)
    sessions = query.offset(skip).limit(limit).all()
    return sessions


@router.get("/{session_id}", response_model=WritingSessionResponse)
async def get_writing_session(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific writing session by ID.
    
    Args:
        session_id: ID of the writing session
        db: Database session
    
    Returns:
        Writing session
    """
    session = db.query(WritingSession).filter(WritingSession.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Writing session not found")
    return session


@router.post("/{session_id}/assessment", response_model=WritingAssessmentResponse)
async def create_writing_assessment(
    session_id: int,
    assessment: WritingAssessmentCreate,
    db: Session = Depends(get_db)
):
    """
    Create an assessment for a writing session.
    
    Args:
        session_id: ID of the writing session
        assessment: Assessment data
        db: Database session
    
    Returns:
        Created assessment
    """
    # Verify session exists
    session = db.query(WritingSession).filter(WritingSession.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Writing session not found")
    
    db_assessment = WritingAssessment(**assessment.dict(), session_id=session_id)
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment


@router.get("/{session_id}/assessment", response_model=WritingAssessmentResponse)
async def get_writing_assessment(
    session_id: int,
    db: Session = Depends(get_db)
):
    """
    Get the assessment for a writing session.
    
    Args:
        session_id: ID of the writing session
        db: Database session
    
    Returns:
        Writing assessment
    """
    assessment = db.query(WritingAssessment).filter(
        WritingAssessment.session_id == session_id
    ).first()
    if assessment is None:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessment 