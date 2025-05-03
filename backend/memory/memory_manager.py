from typing import Dict, Any, List
from sqlalchemy.orm import Session
from models.database import Child, Writing, Assessment


class MemoryManager:
    def __init__(self, session: Session):
        self.session = session
    
    def get_child_writings(self, child_id: int) -> List[Dict[str, Any]]:
        """Retrieve all writings for a child"""
        writings = self.session.query(Writing).filter_by(child_id=child_id).all()
        return [{
            "id": w.id,
            "title": w.title,
            "content": w.content,
            "writing_mode": w.writing_mode,
            "word_count": w.word_count,
            "created_at": w.created_at,
            "time_spent": w.time_spent
        } for w in writings]
    
    def get_child_assessments(self, child_id: int) -> List[Dict[str, Any]]:
        """Retrieve all assessments for a child"""
        assessments = self.session.query(Assessment).filter_by(child_id=child_id).all()
        return [{
            "id": a.id,
            "writing_id": a.writing_id,
            "grade_level": a.grade_level,
            "grammar_score": a.grammar_score,
            "structure_score": a.structure_score,
            "vocabulary_score": a.vocabulary_score,
            "feedback": a.feedback,
            "created_at": a.created_at
        } for a in assessments]
    
    def save_writing(self, child_id: int, writing_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a new writing sample"""
        writing = Writing(
            child_id=child_id,
            title=writing_data.get("title"),
            content=writing_data["content"],
            writing_mode=writing_data["writing_mode"],
            word_count=writing_data.get("word_count"),
            time_spent=writing_data.get("time_spent")
        )
        self.session.add(writing)
        self.session.commit()
        return {
            "id": writing.id,
            "title": writing.title,
            "content": writing.content,
            "writing_mode": writing.writing_mode,
            "word_count": writing.word_count,
            "created_at": writing.created_at,
            "time_spent": writing.time_spent
        }
    
    def save_assessment(self, writing_id: int, child_id: int, assessment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a new assessment"""
        assessment = Assessment(
            writing_id=writing_id,
            child_id=child_id,
            grade_level=assessment_data["grade_level"],
            grammar_score=assessment_data["grammar_score"],
            structure_score=assessment_data["structure_score"],
            vocabulary_score=assessment_data["vocabulary_score"],
            feedback=assessment_data["feedback"]
        )
        self.session.add(assessment)
        self.session.commit()
        return {
            "id": assessment.id,
            "writing_id": assessment.writing_id,
            "grade_level": assessment.grade_level,
            "grammar_score": assessment.grammar_score,
            "structure_score": assessment.structure_score,
            "vocabulary_score": assessment.vocabulary_score,
            "feedback": assessment.feedback,
            "created_at": assessment.created_at
        } 