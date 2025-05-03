from typing import Dict, Any
import logging
from .base_agent import BaseAgent


logger = logging.getLogger(__name__)


class TopicAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.set_system_prompt("""
        You are a creative writing topic generator for children. Your task is to generate engaging and age-appropriate
        writing topics based on the child's interests and grade level. Each topic should include:
        1. A main topic title
        2. A brief description
        3. 2-3 writing prompts or suggestions
        4. Difficulty level (easy, medium, hard)
        5. Estimated time to complete

        Make the topics fun, educational, and tailored to the child's interests. Encourage creativity and imagination.
        """)

    async def generate_topic(self, child_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a writing topic based on child's information.

        Args:
            child_info: Dictionary containing child's age, interests, and grade level

        Returns:
            Dictionary containing the generated topic and related information
        """
        prompt = f"""
        Generate a writing topic for a {child_info['age']}-year-old child in {child_info['grade_level']}.
        The child is interested in: {', '.join(child_info['interests'])}.

        Please provide the topic in the following JSON format:
        {{
            "topic": "topic title",
            "description": "brief description",
            "suggestions": ["prompt 1", "prompt 2", "prompt 3"],
            "difficulty": "easy/medium/hard",
            "estimated_time": "time in minutes"
        }}
        """

        response = await self.generate_response(prompt)
        logger.info("Generated response: %s", response)
        print(response)
        # The response should be a JSON string that we can parse
        # In a real implementation, you'd want to add error handling and validation
        return eval(response)  # Note: In production, use json.loads() with proper error handling
