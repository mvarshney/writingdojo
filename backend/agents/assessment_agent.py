from typing import Dict, Any
from .base_agent import BaseAgent

class AssessmentAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.set_system_prompt("""
        You are an expert writing assessment agent for children. Your task is to evaluate 
        children's writing and provide constructive feedback. Consider the child's age, 
        grade level, and writing experience when making assessments.

        Your assessment should focus on:
        1. Grammar and spelling
        2. Story structure and organization
        3. Vocabulary usage
        4. Creativity and originality
        5. Age-appropriate content

        Format your response as a JSON object with the following structure:
        {
            "grade_level": "Appropriate grade level for the writing",
            "grammar_score": "Assessment of grammar (Poor/Fair/Good/Excellent)",
            "structure_score": "Assessment of structure (Poor/Fair/Good/Excellent)",
            "vocabulary_score": "Assessment of vocabulary (Poor/Fair/Good/Excellent)",
            "feedback": "Detailed feedback and suggestions for improvement",
            "strengths": ["List of writing strengths"],
            "areas_for_improvement": ["List of areas that need improvement"]
        }
        """)

    async def assess_writing(self, writing_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess a child's writing and provide feedback.
        
        Args:
            writing_data: Dictionary containing the writing content and child's information
        
        Returns:
            Dict containing the assessment results
        """
        prompt = f"""
        Please assess the following writing from a {writing_data['age']}-year-old child 
        in {writing_data['grade_level']} grade:

        Writing Topic: {writing_data['topic']}
        Writing Content: {writing_data['content']}
        Word Count: {writing_data['word_count']}

        Please provide a detailed assessment focusing on grammar, structure, vocabulary, 
        and overall writing quality appropriate for the child's age and grade level.
        """
        
        response = await self.generate_response(prompt)
        # Parse the JSON response
        # Note: In a real implementation, you would want to add proper JSON parsing
        # and error handling here
        return {"assessment": response, "raw_response": response} 