
from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.agents import run_analysis

app = FastAPI(
    title="AI Incident Analyzer",
    description="Multi-agent DevOps assistant using LangChain",
    version="1.0.0"
)


class IncidentRequest(BaseModel):
    logs: str = Field(
        min_length=1,
        max_length=20000
    )


@app.get("/")
def home():
    return {
        "message": "AI Incident Analyzer is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(request: IncidentRequest):
    return run_analysis(request.logs)
