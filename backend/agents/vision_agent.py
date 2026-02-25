"""
Edge Vision Agent - Simulated
In production: TensorFlow Lite on mobile device
"""
import hashlib


class VisionAgent:
    def __init__(self):
        # Mock landmark database (in production: trained model)
        self.landmarks = {
            "taj_mahal": ["mughal", "islamic", "marble", "mausoleum"],
            "colosseum": ["roman", "amphitheater", "ancient", "gladiator"],
            "great_wall": ["chinese", "defensive", "stone", "ancient"],
            "statue_liberty": ["neoclassical", "copper", "freedom", "modern"],
            "pyramids_giza": ["egyptian", "pharaoh", "limestone", "ancient"]
        }
    
    def recognize(self, image_bytes: bytes) -> dict:
        """
        Simulates edge AI recognition
        In production: MobileNet/CLIP inference
        """
        # Mock recognition based on image hash (for demo)
        image_hash = hashlib.md5(image_bytes).hexdigest()
        mock_id = list(self.landmarks.keys())[int(image_hash, 16) % len(self.landmarks)]
        
        return {
            "object_id": mock_id,
            "confidence": 0.92,
            "visual_tags": self.landmarks[mock_id],
            "processing": "edge",  # Indicates on-device processing
            "privacy": "no_upload"  # Raw image never sent to cloud
        }
    
    def recognize_by_id(self, landmark_id: str) -> dict:
        """Direct lookup for testing"""
        if landmark_id in self.landmarks:
            return {
                "object_id": landmark_id,
                "confidence": 1.0,
                "visual_tags": self.landmarks[landmark_id],
                "processing": "edge"
            }
        return {"error": "Landmark not found"}
