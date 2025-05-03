from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base


class WritingSession(Base):
    __tablename__ = "writing_sessions"

    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey("child_profiles.id"))
    topic = Column(String)
    content = Column(Text)
    duration = Column(Integer)  # Duration in seconds
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    child = relationship("ChildProfile", back_populates="writing_sessions")
    assessments = relationship("WritingAssessment", back_populates="writing_session") 