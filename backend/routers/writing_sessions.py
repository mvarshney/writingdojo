from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.writing_session import WritingSession
from ..models.writing_assessment import WritingAssessment
from ..models.child_profile import ChildProfile
from ..schemas.writing_session import WritingSessionCreate, WritingSessionResponse
from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)


@router.post("/", response_model=WritingSessionResponse)
def create_writing_session(writing_session: WritingSessionCreate, db: Session = Depends(get_db)):
    """Create a new writing session."""
    # Verify child exists
    child = db.query(ChildProfile).filter(ChildProfile.id == writing_session.child_id).first()
    if not child:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    db_writing_session = WritingSession(**writing_session.dict())
    db.add(db_writing_session)
    db.commit()
    db.refresh(db_writing_session)
    return db_writing_session


@router.get("/", response_model=List[WritingSessionResponse])
def get_writing_sessions(db: Session = Depends(get_db)):
    """Get all writing sessions."""
    return db.query(WritingSession).all()


@router.get("/{writing_session_id}", response_model=WritingSessionResponse)
def get_writing_session(writing_session_id: int, db: Session = Depends(get_db)):
    """Get a specific writing session by ID."""
    writing_session = db.query(WritingSession).filter(WritingSession.id == writing_session_id).first()
    if not writing_session:
        raise HTTPException(status_code=404, detail="Writing session not found")
    return writing_session


@router.put("/{writing_session_id}", response_model=WritingSessionResponse)
def update_writing_session(
    writing_session_id: int,
    writing_session: WritingSessionCreate,
    db: Session = Depends(get_db)
):
    """Update a writing session."""
    db_writing_session = db.query(WritingSession).filter(WritingSession.id == writing_session_id).first()
    if not db_writing_session:
        raise HTTPException(status_code=404, detail="Writing session not found")
    
    for key, value in writing_session.dict().items():
        setattr(db_writing_session, key, value)
    
    db.commit()
    db.refresh(db_writing_session)
    return db_writing_session


@router.delete("/{writing_session_id}")
def delete_writing_session(writing_session_id: int, db: Session = Depends(get_db)):
    """Delete a writing session."""
    writing_session = db.query(WritingSession).filter(WritingSession.id == writing_session_id).first()
    if not writing_session:
        raise HTTPException(status_code=404, detail="Writing session not found")
    
    db.delete(writing_session)
    db.commit()
    return {"message": "Writing session deleted successfully"}


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