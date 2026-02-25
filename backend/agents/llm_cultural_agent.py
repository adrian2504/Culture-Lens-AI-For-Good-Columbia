"""
LLM-Powered Cultural Interpretation Agent
Uses OpenAI/Anthropic/Local LLM for dynamic interpretations
"""
import os
from typing import Optional


class LLMCulturalAgent:
    def __init__(self, provider="openai"):
        self.provider = provider
        
        if provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = "gpt-4o-mini"
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
        
        if self.provider == "anthropic":
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            narrative = response.content[0].text
        else:  # OpenAI or local
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            narrative = response.choices[0].message.content
        
        return {
            "perspective": self._get_perspective_name(lens),
            "narrative": narrative.strip(),
            "emotional_context": self._extract_emotion(narrative),
            "generated_by": f"{self.provider}/{self.model}"
        }
    
    def _build_prompt(self, object_id: str, lens: str, facts: dict) -> str:
        """Build culturally-aware prompt"""
        
        lens_instructions = {
            "local": "Emphasize local community perspectives, national identity, lived experiences, and contemporary relevance. Focus on how local people relate to this heritage today.",
            "asian": "Provide an Asian cultural perspective, emphasizing regional context, historical connections across Asia, aesthetic traditions, and how this fits into broader Asian heritage.",
            "european": "Offer a European perspective, focusing on architectural analysis, historical parallels to European heritage, and how European scholars and visitors have interpreted this site.",
            "indigenous": "Center indigenous and pre-colonial perspectives, highlighting displaced communities, land history, and narratives often overlooked in dominant historical accounts.",
            "neutral": "Provide an academic, neutral interpretation focusing on verified historical facts without cultural bias."
        }
        
        instruction = lens_instructions.get(lens, lens_instructions["neutral"])
        
        return f"""You are a culturally-aware heritage guide. Provide a {lens} cultural interpretation of the following monument.

Monument: {facts.get('name', object_id)}
Location: {facts.get('location', 'Unknown')}
Built: {facts.get('built', 'Unknown')}
Historical Context: {facts.get('summary', 'No summary available')}

Cultural Lens: {lens.upper()}
Instructions: {instruction}

Write a 3-4 sentence interpretation that:
1. Respects the chosen cultural perspective
2. Provides meaningful context beyond basic facts
3. Acknowledges emotional and cultural significance
4. Avoids stereotypes and oversimplification

Interpretation:"""
    
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
        """Simple emotion extraction (could use sentiment analysis)"""
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
