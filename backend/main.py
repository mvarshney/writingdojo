from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import (
    agents_router,
    child_profiles_router,
    writing_sessions_router,
    progress_reports_router
)
from .config import get_settings

app = FastAPI(
    title="Writing Dojo API",
    description="API for the Writing Dojo application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(agents_router)
app.include_router(child_profiles_router)
app.include_router(writing_sessions_router)
app.include_router(progress_reports_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Writing Dojo API"} 