"""
Knowledge Retrieval Agent
Fetches verified historical facts from JSON database or generates using AI
"""
import os
import json
from pathlib import Path
from openai import OpenAI


class KnowledgeAgent:
    def __init__(self):
        # Initialize OpenAI for dynamic fact generation
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None
        
        # Load knowledge base from JSON file
        data_path = Path(__file__).parent.parent / "data" / "landmarks.json"
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.knowledge_db = json.load(f)
            print(f"✅ Loaded {len(self.knowledge_db)} landmarks from database")
        except FileNotFoundError:
            print("⚠️  landmarks.json not found, will use AI for all landmarks")
            self.knowledge_db = {}
        except json.JSONDecodeError as e:
            print(f"⚠️  Error parsing landmarks.json: {e}")
            self.knowledge_db = {}
    
    def get_facts(self, object_id: str, detected_name: str = None, location: str = None) -> dict:
        """Retrieve facts from database or generate dynamically"""
        # Try database first
        facts = self.knowledge_db.get(object_id)
        
        if facts:
            facts["summary"] = self._generate_neutral_summary(facts)
            return facts
        
        # If not in database, generate using AI
        if self.client and detected_name:
            return self._generate_facts_from_ai(detected_name, location)
        
        # Fallback
        return {
            "error": "No knowledge available for this landmark",
            "name": detected_name or object_id,
            "location": location or "Unknown"
        }
    
    def _generate_facts_from_ai(self, landmark_name: str, location: str = None) -> dict:
        """Generate facts using GPT-4o when landmark not in database"""
        try:
            prompt = f"""Provide factual information about: {landmark_name}
{f'Location: {location}' if location else ''}

Respond in this exact format:
NAME: [Official name]
LOCATION: [City, Country]
BUILT: [Construction period]
BUILDER: [Who built it]
PURPOSE: [Original purpose]
STYLE: [Architectural/artistic style]
MATERIAL: [Primary materials]
UNESCO: [Yes/No]

Keep responses factual and concise."""

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a factual encyclopedia providing verified historical information."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.1
            )
            
            content = response.choices[0].message.content.strip()
            facts = self._parse_facts(content, landmark_name)
            facts["summary"] = self._generate_neutral_summary(facts)
            facts["sources"] = ["AI-generated from GPT-4o-mini", "Verification recommended"]
            
            return facts
            
        except Exception as e:
            print(f"AI fact generation error: {e}")
            return {
                "name": landmark_name,
                "location": location or "Unknown",
                "error": "Could not generate facts"
            }
    
    def _parse_facts(self, content: str, default_name: str) -> dict:
        """Parse AI-generated facts"""
        lines = content.split('\n')
        facts = {
            "name": default_name,
            "location": "Unknown",
            "built": "Unknown",
            "builder": "Unknown",
            "purpose": "Unknown",
            "style": "Unknown",
            "material": "Unknown",
            "unesco": False
        }
        
        for line in lines:
            if line.startswith("NAME:"):
                facts["name"] = line.replace("NAME:", "").strip()
            elif line.startswith("LOCATION:"):
                facts["location"] = line.replace("LOCATION:", "").strip()
            elif line.startswith("BUILT:"):
                facts["built"] = line.replace("BUILT:", "").strip()
            elif line.startswith("BUILDER:"):
                facts["builder"] = line.replace("BUILDER:", "").strip()
            elif line.startswith("PURPOSE:"):
                facts["purpose"] = line.replace("PURPOSE:", "").strip()
            elif line.startswith("STYLE:"):
                facts["style"] = line.replace("STYLE:", "").strip()
            elif line.startswith("MATERIAL:"):
                facts["material"] = line.replace("MATERIAL:", "").strip()
            elif line.startswith("UNESCO:"):
                unesco_val = line.replace("UNESCO:", "").strip().lower()
                facts["unesco"] = unesco_val in ["yes", "true"]
        
        return facts
    
    def _generate_neutral_summary(self, facts: dict) -> str:
        """Generate factual summary"""
        return (
            f"The {facts['name']} is located in {facts['location']}. "
            f"Built between {facts['built']}, it was constructed by {facts['builder']} "
            f"as a {facts['purpose']}. The structure exemplifies {facts['style']} "
            f"and is primarily made of {facts['material']}."
        )
