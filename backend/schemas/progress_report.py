from pydantic import BaseModel
from typing import List


class ProgressReportResponse(BaseModel):
    child_id: int
    total_sessions: int
    average_score: float
    areas_for_improvement: List[str]
    strengths: List[str] 