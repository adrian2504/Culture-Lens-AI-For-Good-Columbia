"""
Vision Agent - Real Image Recognition using OpenAI Vision API
"""
import os
import base64
from openai import OpenAI


class VisionAgent:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key)
    
    def recognize(self, image_bytes: bytes) -> dict:
        """
        Real image recognition using OpenAI Vision API (GPT-4o)
        """
        try:
            print(f"🔍 Analyzing image ({len(image_bytes)} bytes)...")
            
            # Encode image to base64
            base64_image = base64.b64encode(image_bytes).decode('utf-8')
            
            # Call OpenAI Vision API with GPT-4o (best vision model)
            print("📡 Calling GPT-4o Vision API...")
            response = self.client.chat.completions.create(
                model="gpt-4o",  # Full vision model, not mini
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert at identifying famous landmarks, monuments, and cultural heritage sites from photographs. Be precise and accurate."
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """Look carefully at this image and identify the specific landmark, monument, or cultural heritage site shown.

Respond in this EXACT format:
NAME: [Official name of the landmark]
LOCATION: [City, Country]
CONFIDENCE: [High/Medium/Low]
DESCRIPTION: [One sentence describing what you see in the image]

Examples:
- If you see the Statue of Liberty: "NAME: Statue of Liberty"
- If you see the Eiffel Tower: "NAME: Eiffel Tower"
- If you see the Taj Mahal: "NAME: Taj Mahal"

Be specific and accurate. If you cannot identify it, respond with NAME: Unknown"""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                    "detail": "high"  # High detail for better recognition
                                }
                            }
                        ]
                    }
                ],
                max_tokens=300,
                temperature=0.0  # Zero temperature for most consistent identification
            )
            
            # Parse response
            content = response.choices[0].message.content.strip()
            print(f"🤖 GPT-4o Response:\n{content}\n")
            
            parsed = self._parse_response(content)
            print(f"✅ Identified: {parsed['name']} (Confidence: {parsed['confidence']})")
            
            if parsed["name"].lower() == "unknown" or parsed["confidence"] == "Low":
                return {
                    "error": "Could not identify a known landmark in this image",
                    "detected": parsed["description"],
                    "confidence": 0.0
                }
            
            return {
                "object_id": self._normalize_name(parsed["name"]),
                "detected_name": parsed["name"],
                "location": parsed["location"],
                "description": parsed["description"],
                "confidence": self._confidence_to_score(parsed["confidence"]),
                "processing": "cloud_vision",
                "model": "gpt-4o"
            }
            
        except Exception as e:
            print(f"❌ Vision API Error: {e}")
            return {
                "error": f"Image recognition failed: {str(e)}",
                "confidence": 0.0
            }
    
    def _parse_response(self, content: str) -> dict:
        """Parse structured response from GPT-4o"""
        lines = content.split('\n')
        result = {
            "name": "Unknown",
            "location": "Unknown",
            "confidence": "Low",
            "description": ""
        }
        
        for line in lines:
            if line.startswith("NAME:"):
                result["name"] = line.replace("NAME:", "").strip()
            elif line.startswith("LOCATION:"):
                result["location"] = line.replace("LOCATION:", "").strip()
            elif line.startswith("CONFIDENCE:"):
                result["confidence"] = line.replace("CONFIDENCE:", "").strip()
            elif line.startswith("DESCRIPTION:"):
                result["description"] = line.replace("DESCRIPTION:", "").strip()
        
        return result
    
    def _normalize_name(self, name: str) -> str:
        """Convert landmark name to object_id"""
        # Remove common words and normalize
        name_lower = name.lower()
        name_lower = name_lower.replace("the ", "").replace(" of ", "_")
        name_lower = name_lower.replace(" ", "_")
        name_lower = name_lower.replace("'", "")
        return name_lower
    
    def _confidence_to_score(self, confidence: str) -> float:
        """Convert confidence level to numeric score"""
        mapping = {
            "high": 0.9,
            "medium": 0.7,
            "low": 0.4
        }
        return mapping.get(confidence.lower(), 0.5)
