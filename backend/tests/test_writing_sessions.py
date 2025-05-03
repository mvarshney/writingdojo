import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ..models import ChildProfile, WritingSession, WritingAssessment


@pytest.fixture
def test_child(db_session: Session):
    """
    Create a test child profile.
    """
    child = ChildProfile(
        name="Test Child",
        age=10,
        grade_level="5th grade",
        interests=["reading", "writing"],
        learning_goals=["improve grammar"]
    )
    db_session.add(child)
    db_session.commit()
    return child


def test_create_writing_session(client: TestClient, db_session: Session, test_child):
    """
    Test creating a new writing session.
    """
    session_data = {
        "child_id": test_child.id,
        "topic": "My Summer Vacation",
        "writing_mode": "free",
        "content": "I went to the beach...",
        "word_count": 150,
        "duration": 30
    }
    
    response = client.post("/api/writing-sessions/", json=session_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["child_id"] == session_data["child_id"]
    assert data["topic"] == session_data["topic"]
    assert data["writing_mode"] == session_data["writing_mode"]
    assert data["content"] == session_data["content"]
    assert data["word_count"] == session_data["word_count"]
    assert data["duration"] == session_data["duration"]
    assert "id" in data
    assert "created_at" in data


def test_get_writing_sessions(client: TestClient, db_session: Session, test_child):
    """
    Test getting a list of writing sessions.
    """
    # Create test sessions
    session1 = WritingSession(
        child_id=test_child.id,
        topic="My Pet",
        writing_mode="free",
        content="I have a dog...",
        word_count=100,
        duration=20
    )
    session2 = WritingSession(
        child_id=test_child.id,
        topic="My Favorite Book",
        writing_mode="guided",
        content="I love reading...",
        word_count=200,
        duration=40
    )
    
    db_session.add(session1)
    db_session.add(session2)
    db_session.commit()
    
    response = client.get(f"/api/writing-sessions/?child_id={test_child.id}")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 2
    assert data[0]["topic"] == "My Pet"
    assert data[1]["topic"] == "My Favorite Book"


def test_get_writing_session(client: TestClient, db_session: Session, test_child):
    """
    Test getting a specific writing session.
    """
    # Create a test session
    session = WritingSession(
        child_id=test_child.id,
        topic="My Summer Vacation",
        writing_mode="free",
        content="I went to the beach...",
        word_count=150,
        duration=30
    )
    
    db_session.add(session)
    db_session.commit()
    
    response = client.get(f"/api/writing-sessions/{session.id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["topic"] == session.topic
    assert data["content"] == session.content
    assert data["word_count"] == session.word_count


def test_create_writing_assessment(client: TestClient, db_session: Session, test_child):
    """
    Test creating a writing assessment.
    """
    # Create a test session
    session = WritingSession(
        child_id=test_child.id,
        topic="My Summer Vacation",
        writing_mode="free",
        content="I went to the beach...",
        word_count=150,
        duration=30
    )
    
    db_session.add(session)
    db_session.commit()
    
    assessment_data = {
        "grade_level": "5th grade",
        "grammar_score": "Good",
        "structure_score": "Excellent",
        "vocabulary_score": "Fair",
        "feedback": "Great job! Keep practicing...",
        "strengths": ["Good story structure", "Clear narrative"],
        "areas_for_improvement": ["Vocabulary usage", "Grammar"]
    }
    
    response = client.post(
        f"/api/writing-sessions/{session.id}/assessment",
        json=assessment_data
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["grade_level"] == assessment_data["grade_level"]
    assert data["grammar_score"] == assessment_data["grammar_score"]
    assert data["structure_score"] == assessment_data["structure_score"]
    assert data["vocabulary_score"] == assessment_data["vocabulary_score"]
    assert data["feedback"] == assessment_data["feedback"]
    assert data["strengths"] == assessment_data["strengths"]
    assert data["areas_for_improvement"] == assessment_data["areas_for_improvement"]
    assert "id" in data
    assert "created_at" in data


def test_get_writing_assessment(client: TestClient, db_session: Session, test_child):
    """
    Test getting a writing assessment.
    """
    # Create a test session and assessment
    session = WritingSession(
        child_id=test_child.id,
        topic="My Summer Vacation",
        writing_mode="free",
        content="I went to the beach...",
        word_count=150,
        duration=30
    )
    
    db_session.add(session)
    db_session.commit()
    
    assessment = WritingAssessment(
        session_id=session.id,
        grade_level="5th grade",
        grammar_score="Good",
        structure_score="Excellent",
        vocabulary_score="Fair",
        feedback="Great job! Keep practicing...",
        strengths=["Good story structure", "Clear narrative"],
        areas_for_improvement=["Vocabulary usage", "Grammar"]
    )
    
    db_session.add(assessment)
    db_session.commit()
    
    response = client.get(f"/api/writing-sessions/{session.id}/assessment")
    assert response.status_code == 200
    
    data = response.json()
    assert data["grade_level"] == assessment.grade_level
    assert data["grammar_score"] == assessment.grammar_score
    assert data["structure_score"] == assessment.structure_score
    assert data["vocabulary_score"] == assessment.vocabulary_score
    assert data["feedback"] == assessment.feedback 