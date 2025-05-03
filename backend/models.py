from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class ChildProfile(Base):
    __tablename__ = "child_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    grade_level = Column(String)
    interests = Column(JSON)
    learning_goals = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    writing_sessions = relationship("WritingSession", back_populates="child")


class WritingSession(Base):
    __tablename__ = "writing_sessions"

    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey("child_profiles.id"))
    topic = Column(String)
    writing_mode = Column(String)
    content = Column(Text)
    word_count = Column(Integer)
    duration = Column(Integer)  # in minutes
    created_at = Column(DateTime, default=datetime.utcnow)

    child = relationship("ChildProfile", back_populates="writing_sessions")
    assessment = relationship("WritingAssessment", back_populates="session", uselist=False)


class WritingAssessment(Base):
    __tablename__ = "writing_assessments"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("writing_sessions.id"))
    grade_level = Column(String)
    grammar_score = Column(String)
    structure_score = Column(String)
    vocabulary_score = Column(String)
    feedback = Column(Text)
    strengths = Column(JSON)
    areas_for_improvement = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("WritingSession", back_populates="assessment")


class ProgressReport(Base):
    __tablename__ = "progress_reports"

    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey("child_profiles.id"))
    overall_progress = Column(JSON)
    strength_areas = Column(JSON)
    improvement_areas = Column(JSON)
    milestones = Column(JSON)
    recommendations = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    child = relationship("ChildProfile") 