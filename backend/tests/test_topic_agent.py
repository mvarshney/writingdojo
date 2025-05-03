import pytest
import logging
from ..agents.topic_agent import TopicAgent


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def topic_agent():
    return TopicAgent()


@pytest.mark.asyncio
async def test_generate_topic(topic_agent):
    """
    Test generating a writing topic.
    """
    child_info = {
        "age": 10,
        "interests": ["animals", "space", "adventure"],
        "grade_level": "5th grade"
    }

    logger.info("Testing topic generation with child info: %s", child_info)
    result = await topic_agent.generate_topic(child_info)
    logger.info("Generated topic result: %s", result)

    # Verify the response structure
    assert "topic" in result
    assert "description" in result
    assert "suggestions" in result
    assert "difficulty" in result
    assert "estimated_time" in result

    # Verify the content
    assert isinstance(result["topic"], str)
    assert isinstance(result["description"], str)
    assert isinstance(result["suggestions"], list)
    assert len(result["suggestions"]) >= 2
    assert result["difficulty"] in ["easy", "medium", "hard"]
    assert "minutes" in result["estimated_time"].lower()
