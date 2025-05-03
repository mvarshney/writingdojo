from typing import Dict, Any, List
from .base_agent import BaseAgent


class ProgressAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.set_system_prompt("""
        You are an expert progress tracking agent for children's writing development. 
        Your task is to analyze writing progress over time and provide insights about 
        improvement areas and achievements.

        Your analysis should:
        1. Track progress across multiple writing sessions
        2. Identify patterns in strengths and areas for improvement
        3. Compare current performance with past performance
        4. Suggest focus areas for future writing sessions
        5. Celebrate milestones and achievements

        Format your response as a JSON object with the following structure:
        {
            "overall_progress": {
                "trend": "Improving/Stable/Needs Attention",
                "summary": "Overall progress summary"
            },
            "strength_areas": [
                {
                    "area": "Writing area",
                    "progress": "Progress description",
                    "evidence": "Specific examples"
                }
            ],
            "improvement_areas": [
                {
                    "area": "Writing area",
                    "current_level": "Current performance",
                    "suggested_focus": "Suggested focus areas"
                }
            ],
            "milestones": [
                {
                    "achievement": "Milestone description",
                    "date": "When achieved",
                    "significance": "Why it's important"
                }
            ],
            "recommendations": [
                "List of specific recommendations for future writing sessions"
            ]
        }
        """)

    async def analyze_progress(
        self, 
        child_data: Dict[str, Any], 
        writing_history: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze writing progress over time.
        
        Args:
            child_data: Dictionary containing the child's information
            writing_history: List of dictionaries containing past writing sessions
        
        Returns:
            Dict containing the progress analysis
        """
        prompt = f"""
        Please analyze the writing progress for {child_data['name']}, 
        a {child_data['age']}-year-old child in {child_data['grade_level']} grade.

        Writing History:
        {writing_history}

        Please provide a comprehensive analysis of their progress, highlighting 
        achievements, areas for improvement, and specific recommendations for 
        future writing sessions.
        """
        
        response = await self.generate_response(prompt)
        # Parse the JSON response
        # Note: In a real implementation, you would want to add proper JSON parsing
        # and error handling here
        return {"progress_analysis": response, "raw_response": response} 