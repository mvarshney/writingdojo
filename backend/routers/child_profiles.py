from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import ChildProfile
from pydantic import BaseModel
from datetime import datetime


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

    class Config:
        orm_mode = True


@router.post("/", response_model=ChildProfileResponse)
async def create_child_profile(
    profile: ChildProfileCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new child profile.
    
    Args:
        profile: Child profile data
        db: Database session
    
    Returns:
        Created child profile
    """
    db_profile = ChildProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


@router.get("/", response_model=List[ChildProfileResponse])
async def get_child_profiles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get a list of child profiles.
    
    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session
    
    Returns:
        List of child profiles
    """
    profiles = db.query(ChildProfile).offset(skip).limit(limit).all()
    return profiles


@router.get("/{profile_id}", response_model=ChildProfileResponse)
async def get_child_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific child profile by ID.
    
    Args:
        profile_id: ID of the child profile
        db: Database session
    
    Returns:
        Child profile
    """
    profile = db.query(ChildProfile).filter(ChildProfile.id == profile_id).first()
    if profile is None:
        raise HTTPException(status_code=404, detail="Child profile not found")
    return profile


@router.put("/{profile_id}", response_model=ChildProfileResponse)
async def update_child_profile(
    profile_id: int,
    profile: ChildProfileUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a child profile.
    
    Args:
        profile_id: ID of the child profile
        profile: Updated profile data
        db: Database session
    
    Returns:
        Updated child profile
    """
    db_profile = db.query(ChildProfile).filter(ChildProfile.id == profile_id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    for key, value in profile.dict().items():
        setattr(db_profile, key, value)
    
    db.commit()
    db.refresh(db_profile)
    return db_profile


@router.delete("/{profile_id}")
async def delete_child_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a child profile.
    
    Args:
        profile_id: ID of the child profile
        db: Database session
    
    Returns:
        Success message
    """
    db_profile = db.query(ChildProfile).filter(ChildProfile.id == profile_id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Child profile not found")
    
    db.delete(db_profile)
    db.commit()
    return {"message": "Child profile deleted successfully"} 