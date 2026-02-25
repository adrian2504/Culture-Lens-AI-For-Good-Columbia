"""
LLM-Powered Cultural Interpretation Agent
Uses OpenAI for dynamic interpretations with efficient prompting
"""
import os
from typing import Optional


class LLMCulturalAgent:
    def __init__(self, provider="openai"):
        self.provider = provider
        
        if provider == "openai":
            from openai import OpenAI
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            self.client = OpenAI(api_key=api_key)
            self.model = "gpt-4o-mini"  # Fast and cost-effective
        elif provider == "anthropic":
            from anthropic import Anthropic
            self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            self.model = "claude-3-5-sonnet-20241022"
        elif provider == "local":
            # Use Ollama or LM Studio
            from openai import OpenAI
            self.client = OpenAI(
                base_url="http://localhost:11434/v1",  # Ollama
                api_key="ollama"
            )
            self.model = "llama3.2"
    
    def interpret(self, object_id: str, lens: str, facts: dict) -> dict:
        """Generate culturally adaptive interpretation using LLM"""
        
        prompt = self._build_prompt(object_id, lens, facts)
        
        try:
            if self.provider == "anthropic":
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=400,
                    messages=[{"role": "user", "content": prompt}]
                )
                narrative = response.content[0].text
            else:  # OpenAI or local
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a culturally-aware heritage guide providing respectful, nuanced interpretations from diverse perspectives."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=400
                )
                narrative = response.choices[0].message.content
            
            return {
                "perspective": self._get_perspective_name(lens),
                "narrative": narrative.strip(),
                "emotional_context": self._extract_emotion(narrative),
                "generated_by": f"{self.provider}/{self.model}"
            }
        except Exception as e:
            print(f"LLM Error: {e}")
            return {
                "perspective": self._get_perspective_name(lens),
                "narrative": f"Error generating interpretation: {str(e)}",
                "emotional_context": "Error",
                "generated_by": f"{self.provider}/error"
            }
    
    def _build_prompt(self, object_id: str, lens: str, facts: dict) -> str:
        """Build culturally-aware prompt with efficient token usage"""
        
        lens_instructions = {
            "local": "Local community: national identity, lived experiences, contemporary relevance, how locals relate to this heritage today.",
            "asian": "Asian perspective: regional context, historical connections across Asia, aesthetic traditions, shared heritage.",
            "european": "European view: architectural analysis, historical parallels, how European scholars interpret this site.",
            "indigenous": "Indigenous lens: pre-colonial perspectives, displaced communities, land history, overlooked narratives.",
            "neutral": "Academic/neutral: verified historical facts without cultural bias."
        }
        
        instruction = lens_instructions.get(lens, lens_instructions["neutral"])
        
        # Efficient prompt - minimal tokens, clear instructions
        return f"""Heritage site: {facts.get('name')}
Location: {facts.get('location')}
Built: {facts.get('built')}
Context: {facts.get('purpose')}

Lens: {lens.upper()}
Focus: {instruction}

Write 3-4 sentences providing meaningful cultural context beyond basic facts. Be respectful, avoid stereotypes, acknowledge emotional significance."""
    
    def _get_perspective_name(self, lens: str) -> str:
        names = {
            "local": "Local Community Perspective",
            "asian": "Asian Cultural Context",
            "european": "European Perspective",
            "indigenous": "Indigenous Perspective",
            "neutral": "Academic/Neutral"
        }
        return names.get(lens, f"{lens.title()} Perspective")
    
    def _extract_emotion(self, narrative: str) -> str:
        """Simple emotion extraction"""
        emotion_keywords = {
            "pride": ["pride", "proud", "achievement", "glory"],
            "reverence": ["sacred", "reverence", "respect", "honor"],
            "complexity": ["complex", "nuanced", "contested", "layered"],
            "loss": ["loss", "displaced", "erased", "forgotten"],
            "wonder": ["wonder", "marvel", "magnificent", "awe"]
        }
        
        narrative_lower = narrative.lower()
        detected = []
        
        for emotion, keywords in emotion_keywords.items():
            if any(kw in narrative_lower for kw in keywords):
                detected.append(emotion)
        
        return ", ".join(detected) if detected else "Cultural reflection"
    
    def get_available_lenses(self, object_id: str) -> list:
        """All lenses available with LLM"""
        return ["local", "asian", "european", "indigenous"]
