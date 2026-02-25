from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
import uvicorn
import os
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables
load_dotenv()

from agents.vision_agent import VisionAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.cultural_agent import CulturalAgent
from agents.bias_agent import BiasAgent
from agents.community_agent import CommunityAgent
from agents.audio_agent import AudioAgent

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
audio_agent = AudioAgent()

# Choose cultural agent: LLM or hardcoded
if USE_LLM:
    provider = os.getenv("LLM_PROVIDER", "openai")
    try:
        cultural_agent = LLMCulturalAgent(provider=provider)
        print(f"✅ Using LLM Cultural Agent ({provider})")
    except Exception as e:
        print(f"⚠️  LLM initialization failed: {e}")
        print("⚠️  Falling back to hardcoded cultural agent")
        cultural_agent = CulturalAgent()
else:
    cultural_agent = CulturalAgent()
    print("✅ Using Hardcoded Cultural Agent (fast demo mode)")

bias_agent = BiasAgent()
community_agent = CommunityAgent()


class AnalysisRequest(BaseModel):
    object_id: str
    cultural_lens: str = "neutral"
    user_context: Optional[dict] = None


class AudioRequest(BaseModel):
    object_id: str
    language: str = "english"
    cultural_lens: str = "local"


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
    
    # 1. Knowledge Retrieval (pass detected name if available)
    facts = knowledge_agent.get_facts(
        request.object_id,
        detected_name=request.user_context.get("detected_name") if request.user_context else None,
        location=request.user_context.get("location") if request.user_context else None
    )
    
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
    
    # 4. Community Sentiment
    community_sentiment = community_agent.get_sentiment(request.object_id)
    
    return {
        "object_id": request.object_id,
        "facts": facts,
        "interpretation": interpretation,
        "bias_report": bias_report,
        "community_sentiment": community_sentiment,
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


@app.get("/audio/languages")
def get_audio_languages():
    """Get available languages for audio narration"""
    return {
        "languages": audio_agent.get_available_languages()
    }


@app.post("/audio/intro")
def generate_intro_audio(request: AudioRequest):
    """Generate introduction audio for a landmark"""
    # Get landmark facts
    facts = knowledge_agent.get_facts(request.object_id)
    
    # Generate intro text
    intro_text = audio_agent.generate_landmark_intro(
        facts.get('name', 'this landmark'),
        facts.get('location', 'an amazing place')
    )
    
    # Generate audio
    audio_data = audio_agent.create_audio_response(intro_text, request.language)
    
    if audio_data:
        return StreamingResponse(
            BytesIO(audio_data),
            media_type="audio/mpeg",
            headers={"Content-Disposition": f"attachment; filename=intro_{request.object_id}.mp3"}
        )
    else:
        return {"error": "Failed to generate audio", "text": intro_text}


@app.post("/audio/narrate")
def generate_narration_audio(request: AudioRequest):
    """Generate full narration audio for a landmark in specified language"""
    # Get landmark data
    facts = knowledge_agent.get_facts(request.object_id)
    interpretation = cultural_agent.interpret(
        object_id=request.object_id,
        lens=request.cultural_lens,
        facts=facts
    )
    
    # Generate narration text
    narration_text = audio_agent.generate_narration({
        'facts': facts,
        'interpretation': interpretation
    }, request.language)
    
    # Generate audio
    audio_data = audio_agent.create_audio_response(narration_text, request.language)
    
    if audio_data:
        return StreamingResponse(
            BytesIO(audio_data),
            media_type="audio/mpeg",
            headers={"Content-Disposition": f"attachment; filename=narration_{request.object_id}_{request.language}.mp3"}
        )
    else:
        return {"error": "Failed to generate audio", "text": narration_text}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
