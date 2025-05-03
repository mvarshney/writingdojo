from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime

from ..database import get_db
from ..models.child_profile import ChildProfile
from ..schemas.child_profile import ChildProfileCreate, ChildProfileResponse

router = APIRouter(prefix="/api/child-profiles", tags=["child-profiles"])


class ChildProfileBase(BaseModel):
    name: str
    age: int
    grade_level: str
    interests: list
    learning_goals: list


class ChildProfileCreate(ChildProfileBase):
    pass


class ChildProfileUpdate(ChildProfileBase):
    pass


class ChildProfileResponse(ChildProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


@router.post("/", response_model=ChildProfileResponse)
def create_child_profile(child_profile: ChildProfileCreate, db: Session = Depends(get_db)):
    """Create a new child profile."""
    db_child_profile = ChildProfile(**child_profile.dict())
    db.add(db_child_profile)
    db.commit()
    db.refresh(db_child_profile)
    return db_child_profile


@router.get("/", response_model=List[ChildProfileResponse])
def get_child_profiles(db: Session = Depends(get_db)):
    """Get all child profiles."""
    return db.query(ChildProfile).all()


@router.get("/{child_profile_id}", response_model=ChildProfileResponse)
def get_child_profile(child_profile_id: int, db: Session = Depends(get_db)):
    """Get a specific child profile by ID."""
    child_profile = db.query(ChildProfile).filter(ChildProfile.id == child_profile_id).first()
    if not child_profile:
        raise HTTPException(status_code=404, detail="Child profile not found")
    return child_profile


@router.put("/{child_profile_id}", response_model=ChildProfileResponse)
def update_child_profile(
    child_profile_id: int,
    child_profile: ChildProfileCreate,
    db: Session = Depends(get_db)
):
    """Update a child profile."""
    db_child_profile = db.query(ChildProfile).filter(ChildProfile.id == child_profile_id).first()
    if not db_child_profile:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    for key, value in child_profile.dict().items():
        setattr(db_child_profile, key, value)
    
    db.commit()
    db.refresh(db_child_profile)
    return db_child_profile


@router.delete("/{child_profile_id}")
def delete_child_profile(child_profile_id: int, db: Session = Depends(get_db)):
    """Delete a child profile."""
    child_profile = db.query(ChildProfile).filter(ChildProfile.id == child_profile_id).first()
    if not child_profile:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    db.delete(child_profile)
    db.commit()
    return {"message": "Child profile deleted successfully"} 