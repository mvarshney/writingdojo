from pydantic import BaseModel, ConfigDict
from datetime import datetime


class WritingSessionBase(BaseModel):
    child_id: int
    topic: str
    content: str
    duration: int


class WritingSessionCreate(WritingSessionBase):
    pass


class WritingSessionResponse(WritingSessionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) 