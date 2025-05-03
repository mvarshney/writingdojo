from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Child(Base):
    __tablename__ = 'children'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    writings = relationship("Writing", back_populates="child")
    assessments = relationship("Assessment", back_populates="child")

class Writing(Base):
    __tablename__ = 'writings'
    
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'))
    title = Column(String(200))
    content = Column(Text, nullable=False)
    writing_mode = Column(String(50), nullable=False)  # creative, essay, story
    word_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    time_spent = Column(Integer)  # in minutes
    
    child = relationship("Child", back_populates="writings")
    assessment = relationship("Assessment", back_populates="writing", uselist=False)

class Assessment(Base):
    __tablename__ = 'assessments'
    
    id = Column(Integer, primary_key=True)
    writing_id = Column(Integer, ForeignKey('writings.id'))
    child_id = Column(Integer, ForeignKey('children.id'))
    grade_level = Column(String(50))
    grammar_score = Column(String(50))
    structure_score = Column(String(50))
    vocabulary_score = Column(String(50))
    feedback = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    writing = relationship("Writing", back_populates="assessment")
    child = relationship("Child", back_populates="assessments")

# Create SQLite database
engine = create_engine('sqlite:///writing_dojo.db')
Base.metadata.create_all(engine) 