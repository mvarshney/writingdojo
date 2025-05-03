import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ..models import ChildProfile, ProgressReport


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


def test_create_progress_report(client: TestClient, db_session: Session, test_child):
    """
    Test creating a new progress report.
    """
    report_data = {
        "child_id": test_child.id,
        "overall_progress": {
            "trend": "Improving",
            "summary": "Showing good progress in writing skills"
        },
        "strength_areas": [
            {
                "area": "Story Structure",
                "progress": "Excellent",
                "evidence": "Well-organized paragraphs"
            }
        ],
        "improvement_areas": [
            {
                "area": "Grammar",
                "current_level": "Fair",
                "suggested_focus": "Verb tense consistency"
            }
        ],
        "milestones": [
            {
                "achievement": "First complete story",
                "date": "2024-01-15",
                "significance": "Demonstrated ability to write a full narrative"
            }
        ],
        "recommendations": [
            "Practice writing daily",
            "Focus on grammar exercises"
        ]
    }
    
    response = client.post("/api/progress-reports/", json=report_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["child_id"] == report_data["child_id"]
    assert data["overall_progress"] == report_data["overall_progress"]
    assert data["strength_areas"] == report_data["strength_areas"]
    assert data["improvement_areas"] == report_data["improvement_areas"]
    assert data["milestones"] == report_data["milestones"]
    assert data["recommendations"] == report_data["recommendations"]
    assert "id" in data
    assert "created_at" in data


def test_get_progress_reports(client: TestClient, db_session: Session, test_child):
    """
    Test getting a list of progress reports.
    """
    # Create test reports
    report1 = ProgressReport(
        child_id=test_child.id,
        overall_progress={
            "trend": "Improving",
            "summary": "Good progress"
        },
        strength_areas=[{"area": "Creativity", "progress": "Excellent"}],
        improvement_areas=[{"area": "Grammar", "current_level": "Fair"}],
        milestones=[{"achievement": "First story", "date": "2024-01-01"}],
        recommendations=["Keep practicing"]
    )
    report2 = ProgressReport(
        child_id=test_child.id,
        overall_progress={
            "trend": "Stable",
            "summary": "Maintaining skills"
        },
        strength_areas=[{"area": "Vocabulary", "progress": "Good"}],
        improvement_areas=[{"area": "Punctuation", "current_level": "Fair"}],
        milestones=[{"achievement": "Improved grammar", "date": "2024-02-01"}],
        recommendations=["Focus on punctuation"]
    )
    
    db_session.add(report1)
    db_session.add(report2)
    db_session.commit()
    
    response = client.get(f"/api/progress-reports/?child_id={test_child.id}")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 2
    assert data[0]["overall_progress"]["trend"] == "Improving"
    assert data[1]["overall_progress"]["trend"] == "Stable"


def test_get_progress_report(client: TestClient, db_session: Session, test_child):
    """
    Test getting a specific progress report.
    """
    # Create a test report
    report = ProgressReport(
        child_id=test_child.id,
        overall_progress={
            "trend": "Improving",
            "summary": "Showing good progress"
        },
        strength_areas=[{"area": "Creativity", "progress": "Excellent"}],
        improvement_areas=[{"area": "Grammar", "current_level": "Fair"}],
        milestones=[{"achievement": "First story", "date": "2024-01-01"}],
        recommendations=["Keep practicing"]
    )
    
    db_session.add(report)
    db_session.commit()
    
    response = client.get(f"/api/progress-reports/{report.id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["overall_progress"] == report.overall_progress
    assert data["strength_areas"] == report.strength_areas
    assert data["improvement_areas"] == report.improvement_areas


def test_update_progress_report(client: TestClient, db_session: Session, test_child):
    """
    Test updating a progress report.
    """
    # Create a test report
    report = ProgressReport(
        child_id=test_child.id,
        overall_progress={
            "trend": "Improving",
            "summary": "Good progress"
        },
        strength_areas=[{"area": "Creativity", "progress": "Excellent"}],
        improvement_areas=[{"area": "Grammar", "current_level": "Fair"}],
        milestones=[{"achievement": "First story", "date": "2024-01-01"}],
        recommendations=["Keep practicing"]
    )
    
    db_session.add(report)
    db_session.commit()
    
    update_data = {
        "child_id": test_child.id,
        "overall_progress": {
            "trend": "Excellent",
            "summary": "Outstanding progress"
        },
        "strength_areas": [
            {
                "area": "Creativity",
                "progress": "Excellent",
                "evidence": "Imaginative stories"
            }
        ],
        "improvement_areas": [
            {
                "area": "Grammar",
                "current_level": "Good",
                "suggested_focus": "Complex sentences"
            }
        ],
        "milestones": [
            {
                "achievement": "Completed novel",
                "date": "2024-02-01",
                "significance": "Major writing achievement"
            }
        ],
        "recommendations": [
            "Continue creative writing",
            "Try different genres"
        ]
    }
    
    response = client.put(f"/api/progress-reports/{report.id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["overall_progress"] == update_data["overall_progress"]
    assert data["strength_areas"] == update_data["strength_areas"]
    assert data["improvement_areas"] == update_data["improvement_areas"]
    assert data["milestones"] == update_data["milestones"]
    assert data["recommendations"] == update_data["recommendations"]


def test_delete_progress_report(client: TestClient, db_session: Session, test_child):
    """
    Test deleting a progress report.
    """
    # Create a test report
    report = ProgressReport(
        child_id=test_child.id,
        overall_progress={
            "trend": "Improving",
            "summary": "Good progress"
        },
        strength_areas=[{"area": "Creativity", "progress": "Excellent"}],
        improvement_areas=[{"area": "Grammar", "current_level": "Fair"}],
        milestones=[{"achievement": "First story", "date": "2024-01-01"}],
        recommendations=["Keep practicing"]
    )
    
    db_session.add(report)
    db_session.commit()
    
    response = client.delete(f"/api/progress-reports/{report.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Progress report deleted successfully"}
    
    # Verify the report was deleted
    deleted_report = db_session.query(ProgressReport).filter_by(id=report.id).first()
    assert deleted_report is None 