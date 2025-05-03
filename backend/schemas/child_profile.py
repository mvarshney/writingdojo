from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ChildProfileBase(BaseModel):
    name: str
    age: int
    grade: str
    interests: str
    learning_style: str


class ChildProfileCreate(ChildProfileBase):
    pass


class ChildProfileResponse(ChildProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) 