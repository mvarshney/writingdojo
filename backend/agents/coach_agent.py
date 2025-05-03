from typing import Dict, Any
from .base_agent import BaseAgent


class CoachAgent(BaseAgent):
    def __init__(self):
        system_message = """You are a writing coach for children.
        Analyze their progress over time and provide personalized strategies for improvement.
        Consider their strengths and areas for growth.
        Suggest specific exercises and reading materials."""
        super().__init__("CoachAgent", system_message)
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: Implement coaching logic
        return {
            "progress_summary": "Showing improvement in vocabulary",
            "strengths": ["Creative ideas", "Good structure"],
            "areas_for_improvement": ["Grammar", "Sentence variety"],
            "suggested_exercises": ["Practice using different sentence structures"],
            "reading_recommendations": ["Age-appropriate books with rich vocabulary"]
        } 