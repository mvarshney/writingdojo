from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base


class WritingAssessment(Base):
    __tablename__ = "writing_assessments"

    id = Column(Integer, primary_key=True, index=True)
    writing_session_id = Column(Integer, ForeignKey("writing_sessions.id"))
    feedback = Column(Text)
    score = Column(Integer)
    areas_for_improvement = Column(Text)
    strengths = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    writing_session = relationship("WritingSession", back_populates="assessments") 