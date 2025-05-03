import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ..models import ChildProfile


def test_create_child_profile(client: TestClient, db_session: Session):
    """
    Test creating a new child profile.
    """
    profile_data = {
        "name": "Test Child",
        "age": 10,
        "grade_level": "5th grade",
        "interests": ["reading", "writing"],
        "learning_goals": ["improve grammar", "expand vocabulary"]
    }
    
    response = client.post("/api/child-profiles/", json=profile_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == profile_data["name"]
    assert data["age"] == profile_data["age"]
    assert data["grade_level"] == profile_data["grade_level"]
    assert data["interests"] == profile_data["interests"]
    assert data["learning_goals"] == profile_data["learning_goals"]
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_get_child_profiles(client: TestClient, db_session: Session):
    """
    Test getting a list of child profiles.
    """
    # Create test profiles
    profile1 = ChildProfile(
        name="Child 1",
        age=8,
        grade_level="3rd grade",
        interests=["drawing", "reading"],
        learning_goals=["improve spelling"]
    )
    profile2 = ChildProfile(
        name="Child 2",
        age=12,
        grade_level="7th grade",
        interests=["writing", "science"],
        learning_goals=["better essays"]
    )
    
    db_session.add(profile1)
    db_session.add(profile2)
    db_session.commit()
    
    response = client.get("/api/child-profiles/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Child 1"
    assert data[1]["name"] == "Child 2"


def test_get_child_profile(client: TestClient, db_session: Session):
    """
    Test getting a specific child profile.
    """
    # Create a test profile
    profile = ChildProfile(
        name="Test Child",
        age=10,
        grade_level="5th grade",
        interests=["reading", "writing"],
        learning_goals=["improve grammar"]
    )
    
    db_session.add(profile)
    db_session.commit()
    
    response = client.get(f"/api/child-profiles/{profile.id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == profile.name
    assert data["age"] == profile.age
    assert data["grade_level"] == profile.grade_level


def test_update_child_profile(client: TestClient, db_session: Session):
    """
    Test updating a child profile.
    """
    # Create a test profile
    profile = ChildProfile(
        name="Test Child",
        age=10,
        grade_level="5th grade",
        interests=["reading"],
        learning_goals=["improve grammar"]
    )
    
    db_session.add(profile)
    db_session.commit()
    
    update_data = {
        "name": "Updated Child",
        "age": 11,
        "grade_level": "6th grade",
        "interests": ["reading", "writing"],
        "learning_goals": ["improve grammar", "expand vocabulary"]
    }
    
    response = client.put(f"/api/child-profiles/{profile.id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["age"] == update_data["age"]
    assert data["grade_level"] == update_data["grade_level"]
    assert data["interests"] == update_data["interests"]
    assert data["learning_goals"] == update_data["learning_goals"]


def test_delete_child_profile(client: TestClient, db_session: Session):
    """
    Test deleting a child profile.
    """
    # Create a test profile
    profile = ChildProfile(
        name="Test Child",
        age=10,
        grade_level="5th grade",
        interests=["reading"],
        learning_goals=["improve grammar"]
    )
    
    db_session.add(profile)
    db_session.commit()
    
    response = client.delete(f"/api/child-profiles/{profile.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Child profile deleted successfully"}
    
    # Verify the profile was deleted
    deleted_profile = db_session.query(ChildProfile).filter_by(id=profile.id).first()
    assert deleted_profile is None 