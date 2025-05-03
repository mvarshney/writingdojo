from typing import Dict, Any
from .base_agent import BaseAgent


class TopicSuggestAgent(BaseAgent):
    def __init__(self):
        system_message = """You are an expert at suggesting engaging writing topics for children.
        Consider the child's age, previous writings, and ensure variety in topics and writing modes.
        Make suggestions that are both educational and fun."""
        super().__init__("TopicSuggestAgent", system_message)
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: Implement topic suggestion logic
        return {
            "topic": "A day in the life of a superhero",
            "writing_mode": "creative",
            "suggested_time": 30
        } 