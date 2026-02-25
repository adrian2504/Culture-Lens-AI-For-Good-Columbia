from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

from agents.vision_agent import VisionAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.cultural_agent import CulturalAgent
from agents.bias_agent import BiasAgent
import os

# Optional: LLM-powered cultural agent
USE_LLM = os.getenv("USE_LLM", "false").lower() == "true"
if USE_LLM:
    from agents.llm_cultural_agent import LLMCulturalAgent

app = FastAPI(title="CultureLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
vision_agent = VisionAgent()
knowledge_agent = KnowledgeAgent()

# Choose cultural agent: LLM or hardcoded
if USE_LLM:
    provider = os.getenv("LLM_PROVIDER", "openai")
    cultural_agent = LLMCulturalAgent(provider=provider)
    print(f"✓ Using LLM Cultural Agent ({provider})")
else:
    cultural_agent = CulturalAgent()
    print("✓ Using Hardcoded Cultural Agent (fast demo mode)")

bias_agent = BiasAgent()


class AnalysisRequest(BaseModel):
    object_id: str
    cultural_lens: str = "neutral"
    user_context: Optional[dict] = None


@app.get("/")
def root():
    return {"message": "CultureLens API", "status": "running"}


@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    """Edge vision simulation - in production this runs on-device"""
    image_bytes = await file.read()
    vision_result = vision_agent.recognize(image_bytes)
    return vision_result


@app.post("/interpret")
def interpret_heritage(request: AnalysisRequest):
    """Multi-agent cultural interpretation pipeline"""
    
    # 1. Knowledge Retrieval
    facts = knowledge_agent.get_facts(request.object_id)
    
    # 2. Cultural Interpretation
    interpretation = cultural_agent.interpret(
        object_id=request.object_id,
        lens=request.cultural_lens,
        facts=facts
    )
    
    # 3. Bias Analysis
    bias_report = bias_agent.analyze(
        object_id=request.object_id,
        lens=request.cultural_lens
    )
    
    return {
        "object_id": request.object_id,
        "facts": facts,
        "interpretation": interpretation,
        "bias_report": bias_report,
        "available_lenses": cultural_agent.get_available_lenses(request.object_id)
    }


@app.get("/lenses")
def get_lenses():
    """Get all available cultural lenses"""
    return {
        "lenses": [
            {"id": "neutral", "name": "Neutral/Academic"},
            {"id": "local", "name": "Local Community"},
            {"id": "asian", "name": "Asian Perspective"},
            {"id": "european", "name": "European Perspective"},
            {"id": "indigenous", "name": "Indigenous Perspective"}
        ]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
