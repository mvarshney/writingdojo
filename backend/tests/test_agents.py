import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from ..agents import (
    TopicAgent,
    AssessmentAgent,
    FeedbackAgent,
    ProgressAgent,
    AgentOrchestrator
)


@pytest.fixture
def topic_agent():
    """
    Create a TopicAgent instance.
    """
    return TopicAgent()


@pytest.fixture
def assessment_agent():
    """
    Create an AssessmentAgent instance.
    """
    return AssessmentAgent()


@pytest.fixture
def feedback_agent():
    """
    Create a FeedbackAgent instance.
    """
    return FeedbackAgent()


@pytest.fixture
def progress_agent():
    """
    Create a ProgressAgent instance.
    """
    return ProgressAgent()


@pytest.fixture
def orchestrator():
    """
    Create an AgentOrchestrator instance.
    """
    return AgentOrchestrator()


def test_topic_agent_generate_topic(topic_agent):
    """
    Test generating a writing topic.
    """
    child_info = {
        "age": 10,
        "interests": ["animals", "space"],
        "grade_level": "5th grade"
    }
    
    with patch.object(topic_agent, "generate_response") as mock_generate:
        mock_generate.return_value = {
            "topic": "A Day in the Life of an Astronaut",
            "description": "Write about what it would be like to be an astronaut",
            "suggestions": [
                "What would you eat in space?",
                "How would you sleep in zero gravity?"
            ],
            "difficulty": "medium",
            "estimated_time": "30 minutes"
        }
        
        result = topic_agent.generate_topic(child_info)
        assert "topic" in result
        assert "description" in result
        assert "suggestions" in result
        assert "difficulty" in result
        assert "estimated_time" in result


def test_assessment_agent_assess_writing(assessment_agent):
    """
    Test assessing a writing sample.
    """
    writing_data = {
        "age": 10,
        "grade_level": "5th grade",
        "topic": "My Summer Vacation",
        "content": "I went to the beach...",
        "word_count": 150
    }
    
    with patch.object(assessment_agent, "generate_response") as mock_generate:
        mock_generate.return_value = {
            "grade_level": "5th grade",
            "grammar_score": "Good",
            "structure_score": "Excellent",
            "vocabulary_score": "Fair",
            "feedback": "Great job! Keep practicing...",
            "strengths": ["Good story structure", "Clear narrative"],
            "areas_for_improvement": ["Vocabulary usage", "Grammar"]
        }
        
        result = assessment_agent.assess_writing(writing_data)
        assert "grade_level" in result
        assert "grammar_score" in result
        assert "structure_score" in result
        assert "vocabulary_score" in result
        assert "feedback" in result
        assert "strengths" in result
        assert "areas_for_improvement" in result


def test_feedback_agent_generate_feedback(feedback_agent):
    """
    Test generating feedback for a writing sample.
    """
    writing_data = {
        "age": 10,
        "grade_level": "5th grade",
        "topic": "My Summer Vacation",
        "content": "I went to the beach...",
        "word_count": 150
    }
    
    assessment_results = {
        "grade_level": "5th grade",
        "grammar_score": "Good",
        "structure_score": "Excellent",
        "vocabulary_score": "Fair",
        "feedback": "Great job! Keep practicing...",
        "strengths": ["Good story structure", "Clear narrative"],
        "areas_for_improvement": ["Vocabulary usage", "Grammar"]
    }
    
    with patch.object(feedback_agent, "generate_response") as mock_generate:
        mock_generate.return_value = {
            "positive_feedback": "Your story has a clear beginning, middle, and end",
            "suggestions": [
                {
                    "area": "Vocabulary",
                    "suggestion": "Try using more descriptive words",
                    "example": "Instead of 'big', try 'enormous' or 'gigantic'"
                }
            ],
            "encouragement": "Keep up the great work!",
            "next_steps": ["Practice using new vocabulary words", "Write another story"]
        }
        
        result = feedback_agent.generate_feedback(writing_data, assessment_results)
        assert "positive_feedback" in result
        assert "suggestions" in result
        assert "encouragement" in result
        assert "next_steps" in result


def test_progress_agent_analyze_progress(progress_agent):
    """
    Test analyzing writing progress.
    """
    child_data = {
        "name": "Test Child",
        "age": 10,
        "grade_level": "5th grade"
    }
    
    writing_history = [
        {
            "date": "2024-01-01",
            "topic": "My Pet",
            "word_count": 100,
            "assessment": {
                "grammar_score": "Fair",
                "structure_score": "Good",
                "vocabulary_score": "Fair"
            }
        },
        {
            "date": "2024-02-01",
            "topic": "My Summer Vacation",
            "word_count": 150,
            "assessment": {
                "grammar_score": "Good",
                "structure_score": "Excellent",
                "vocabulary_score": "Good"
            }
        }
    ]
    
    with patch.object(progress_agent, "generate_response") as mock_generate:
        mock_generate.return_value = {
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
                    "current_level": "Good",
                    "suggested_focus": "Complex sentences"
                }
            ],
            "milestones": [
                {
                    "achievement": "Improved vocabulary",
                    "date": "2024-02-01",
                    "significance": "Using more descriptive words"
                }
            ],
            "recommendations": [
                "Practice writing daily",
                "Focus on grammar exercises"
            ]
        }
        
        result = progress_agent.analyze_progress(child_data, writing_history)
        assert "overall_progress" in result
        assert "strength_areas" in result
        assert "improvement_areas" in result
        assert "milestones" in result
        assert "recommendations" in result


def test_orchestrator_process_writing_session(orchestrator):
    """
    Test processing a complete writing session.
    """
    child_data = {
        "name": "Test Child",
        "age": 10,
        "grade_level": "5th grade"
    }
    
    writing_data = {
        "topic": "My Summer Vacation",
        "content": "I went to the beach...",
        "word_count": 150
    }
    
    writing_history = [
        {
            "date": "2024-01-01",
            "topic": "My Pet",
            "word_count": 100,
            "assessment": {
                "grammar_score": "Fair",
                "structure_score": "Good",
                "vocabulary_score": "Fair"
            }
        }
    ]
    
    with patch.object(orchestrator.assessment_agent, "assess_writing") as mock_assess:
        with patch.object(orchestrator.feedback_agent, "generate_feedback") as mock_feedback:
            with patch.object(orchestrator.progress_agent, "analyze_progress") as mock_progress:
                mock_assess.return_value = {
                    "grade_level": "5th grade",
                    "grammar_score": "Good",
                    "structure_score": "Excellent",
                    "vocabulary_score": "Fair",
                    "feedback": "Great job!",
                    "strengths": ["Good structure"],
                    "areas_for_improvement": ["Grammar"]
                }
                
                mock_feedback.return_value = {
                    "positive_feedback": "Well done!",
                    "suggestions": [{"area": "Grammar", "suggestion": "Practice more"}],
                    "encouragement": "Keep writing!",
                    "next_steps": ["Write daily"]
                }
                
                mock_progress.return_value = {
                    "overall_progress": {"trend": "Improving"},
                    "strength_areas": [{"area": "Structure"}],
                    "improvement_areas": [{"area": "Grammar"}],
                    "milestones": [{"achievement": "First story"}],
                    "recommendations": ["Keep practicing"]
                }
                
                result = orchestrator.process_writing_session(
                    child_data,
                    writing_data,
                    writing_history
                )
                
                assert "assessment" in result
                assert "feedback" in result
                assert "progress" in result 