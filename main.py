from fastapi import FastAPI
from pydantic import BaseModel

from orchestrator import run_content_workflow


app = FastAPI(title="ContentForge")


class ContentRequest(BaseModel):
    topic: str


@app.get("/")
def root():
    return {
        "message": "ContentForge is running"
    }


@app.post("/generate")
def generate(request: ContentRequest):
    return run_content_workflow(request.topic)