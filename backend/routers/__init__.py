from .agents import router as agents_router
from .child_profiles import router as child_profiles_router
from .writing_sessions import router as writing_sessions_router
from .progress_reports import router as progress_reports_router

__all__ = [
    'agents_router',
    'child_profiles_router',
    'writing_sessions_router',
    'progress_reports_router'
] 