from typing import Dict, Any
from .base_agent import BaseAgent

class TopicAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.set_system_prompt("""
        You are a creative writing topic generator for children. Your task is to generate 
        engaging and age-appropriate writing topics that will inspire children to write 
        creative stories. Consider the child's age, interests, and writing level when 
        generating topics.

        The topics should be:
        1. Age-appropriate
        2. Engaging and interesting
        3. Open-ended to encourage creativity
        4. Clear and easy to understand
        5. Relevant to the child's interests

        Format your response as a JSON object with the following structure:
        {
            "topic": "The writing topic",
            "description": "A brief description of the topic",
            "suggestions": ["List of writing suggestions or prompts"],
            "difficulty": "easy/medium/hard",
            "estimated_time": "Estimated time in minutes"
        }
        """)

    async def generate_topic(self, child_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a writing topic based on the child's information.
        
        Args:
            child_info: Dictionary containing child's information (age, interests, etc.)
        
        Returns:
            Dict containing the generated topic and related information
        """
        prompt = f"""
        Generate a writing topic for a {child_info['age']}-year-old child.
        The child's interests include: {', '.join(child_info['interests'])}.
        Their current writing level is: {child_info['grade_level']}.
        """
        
        response = await self.generate_response(prompt)
        # Parse the JSON response
        # Note: In a real implementation, you would want to add proper JSON parsing
        # and error handling here
        return {"topic": response, "raw_response": response} 