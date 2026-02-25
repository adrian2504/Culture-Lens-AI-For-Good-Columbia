"""
Community Sentiment Agent
Aggregates user reflections and emotional responses
"""
import json
from pathlib import Path
from datetime import datetime


class CommunityAgent:
    def __init__(self):
        # Load community sentiment data
        data_path = Path(__file__).parent.parent / "data" / "community_sentiment.json"
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.sentiment_data = json.load(f)
            print(f"✅ Loaded community sentiment for {len(self.sentiment_data)} landmarks")
        except FileNotFoundError:
            print("⚠️  community_sentiment.json not found, using defaults")
            self.sentiment_data = {}
    
    def get_sentiment(self, object_id: str) -> dict:
        """Get aggregated community sentiment for a landmark"""
        sentiment = self.sentiment_data.get(object_id)
        
        if not sentiment:
            return {
                "message": "Be the first to share your perspective on this landmark!",
                "emotions": {},
                "reflections_count": 0
            }
        
        return {
            "emotions": sentiment.get("emotions", {}),
            "common_themes": sentiment.get("themes", []),
            "reflections_count": sentiment.get("count", 0),
            "sample_quotes": sentiment.get("quotes", [])
        }
    
    def add_reflection(self, object_id: str, reflection: dict) -> dict:
        """
        Add user reflection (in production, this would save to database)
        For MVP, we just acknowledge it
        """
        return {
            "status": "received",
            "message": "Thank you for sharing your perspective!",
            "reflection_id": f"{object_id}_{datetime.now().timestamp()}"
        }
