from typing import Dict, Any, List
from .base_agent import BaseAgent
from .topic_agent import TopicAgent
from .assessment_agent import AssessmentAgent
from .feedback_agent import FeedbackAgent
from .progress_agent import ProgressAgent


class AgentOrchestrator:
    def __init__(self):
        self.topic_agent = TopicAgent()
        self.assessment_agent = AssessmentAgent()
        self.feedback_agent = FeedbackAgent()
        self.progress_agent = ProgressAgent()

    async def generate_topic(self, child_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a writing topic for a child.
        
        Args:
            child_data: Dictionary containing the child's information
        
        Returns:
            Dict containing the generated topic
        """
        return await self.topic_agent.generate_topic(child_data)

    async def assess_writing(
        self, 
        writing_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess a child's writing.
        
        Args:
            writing_data: Dictionary containing the writing content and child's information
        
        Returns:
            Dict containing the assessment results
        """
        assessment = await self.assessment_agent.assess_writing(writing_data)
        feedback = await self.feedback_agent.generate_feedback(
            writing_data, 
            assessment["assessment"]
        )
        
        return {
            "assessment": assessment["assessment"],
            "feedback": feedback["feedback"]
        }

    async def analyze_progress(
        self, 
        child_data: Dict[str, Any], 
        writing_history: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze a child's writing progress over time.
        
        Args:
            child_data: Dictionary containing the child's information
            writing_history: List of dictionaries containing past writing sessions
        
        Returns:
            Dict containing the progress analysis
        """
        return await self.progress_agent.analyze_progress(
            child_data, 
            writing_history
        )

    async def process_writing_session(
        self, 
        child_data: Dict[str, Any], 
        writing_data: Dict[str, Any], 
        writing_history: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Process a complete writing session, including assessment, feedback, and progress analysis.
        
        Args:
            child_data: Dictionary containing the child's information
            writing_data: Dictionary containing the writing content
            writing_history: List of dictionaries containing past writing sessions
        
        Returns:
            Dict containing the complete session analysis
        """
        assessment_results = await self.assess_writing(writing_data)
        progress_analysis = await self.analyze_progress(
            child_data, 
            writing_history
        )
        
        return {
            "assessment": assessment_results["assessment"],
            "feedback": assessment_results["feedback"],
            "progress": progress_analysis["progress_analysis"]
        } 