from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from ..agents.orchestrator import AgentOrchestrator

router = APIRouter(prefix="/api/agents", tags=["agents"])
orchestrator = AgentOrchestrator()


@router.post("/generate-topic")
async def generate_topic(child_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a writing topic for a child.
    
    Args:
        child_data: Dictionary containing the child's information
    
    Returns:
        Dict containing the generated topic
    """
    try:
        return await orchestrator.generate_topic(child_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/assess-writing")
async def assess_writing(writing_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Assess a child's writing.
    
    Args:
        writing_data: Dictionary containing the writing content and child's information
    
    Returns:
        Dict containing the assessment results
    """
    try:
        return await orchestrator.assess_writing(writing_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze-progress")
async def analyze_progress(
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
    try:
        return await orchestrator.analyze_progress(child_data, writing_history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/process-session")
async def process_writing_session(
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
    try:
        return await orchestrator.process_writing_session(
            child_data,
            writing_data,
            writing_history
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 