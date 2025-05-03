from typing import Dict, Any, List
from .base_agent import BaseAgent


class FeedbackAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.set_system_prompt("""
        You are an expert writing feedback agent for children. Your task is to provide 
        encouraging and constructive feedback on children's writing. Your feedback should 
        be age-appropriate, positive, and focused on helping the child improve their 
        writing skills while maintaining their enthusiasm for writing.

        Your feedback should:
        1. Start with positive reinforcement
        2. Provide specific suggestions for improvement
        3. Use age-appropriate language
        4. Include examples when helpful
        5. End with encouragement

        Format your response as a JSON object with the following structure:
        {
            "positive_feedback": "Specific praise about what the child did well",
            "suggestions": [
                {
                    "area": "Area for improvement",
                    "suggestion": "Specific suggestion",
                    "example": "Example of how to improve"
                }
            ],
            "encouragement": "Motivational message to keep writing",
            "next_steps": ["List of specific next steps to practice"]
        }
        """)

    async def generate_feedback(
        self, 
        writing_data: Dict[str, Any], 
        assessment_results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate personalized feedback based on writing and assessment.
        
        Args:
            writing_data: Dictionary containing the writing content and child's information
            assessment_results: Dictionary containing the assessment results
        
        Returns:
            Dict containing the feedback and suggestions
        """
        prompt = f"""
        Please provide feedback for a {writing_data['age']}-year-old child 
        in {writing_data['grade_level']} grade based on their writing:

        Writing Topic: {writing_data['topic']}
        Writing Content: {writing_data['content']}
        Word Count: {writing_data['word_count']}

        Assessment Results:
        {assessment_results}

        Please provide encouraging feedback that focuses on their strengths while 
        suggesting specific ways to improve. Make sure your feedback is appropriate 
        for their age and grade level.
        """
        
        response = await self.generate_response(prompt)
        # Parse the JSON response
        # Note: In a real implementation, you would want to add proper JSON parsing
        # and error handling here
        return {"feedback": response, "raw_response": response} 