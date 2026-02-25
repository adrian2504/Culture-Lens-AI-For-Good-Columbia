"""
Bias & Ethics Agent - AI for Good Signal
Provides transparency about source dominance and missing perspectives
"""
import json
from pathlib import Path


class BiasAgent:
    def __init__(self):
        # Load bias data from JSON file
        data_path = Path(__file__).parent.parent / "data" / "bias_data.json"
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.bias_data = json.load(f)
            print(f"✅ Loaded bias data for {len(self.bias_data)} landmarks")
        except FileNotFoundError:
            print("⚠️  bias_data.json not found")
            self.bias_data = {}
        except json.JSONDecodeError as e:
            print(f"⚠️  Error parsing bias_data.json: {e}")
            self.bias_data = {}
    
    def analyze(self, object_id: str, lens: str) -> dict:
        """Analyze bias and provide transparency"""
        bias_info = self.bias_data.get(object_id)
        
        if not bias_info:
            return {
                "transparency_note": "Bias analysis not yet available for this object",
                "recommendation": "Seek multiple sources and perspectives"
            }
        
        # Calculate diversity score
        source_dist = bias_info["source_dominance"]
        diversity_score = self._calculate_diversity(source_dist)
        
        return {
            "source_dominance": bias_info["source_dominance"],
            "diversity_score": diversity_score,
            "missing_perspectives": bias_info["missing_perspectives"],
            "power_imbalances": bias_info["power_imbalances"],
            "representation_gaps": bias_info["representation_gaps"],
            "transparency_note": self._generate_transparency_note(bias_info, lens),
            "recommendation": "Consider exploring multiple cultural lenses for a fuller understanding"
        }
    
    def _calculate_diversity(self, source_dist: dict) -> float:
        """Calculate source diversity score (0-1, higher is more diverse)"""
        # Simple entropy-based calculation
        import math
        entropy = -sum(p * math.log(p) if p > 0 else 0 for p in source_dist.values())
        max_entropy = math.log(len(source_dist))
        return round(entropy / max_entropy, 2) if max_entropy > 0 else 0
    
    def _generate_transparency_note(self, bias_info: dict, lens: str) -> str:
        """Generate human-readable transparency note"""
        dominant_source = max(bias_info["source_dominance"].items(), key=lambda x: x[1])
        
        return (
            f"Most available sources ({int(dominant_source[1]*100)}%) come from {dominant_source[0].replace('_', ' ')} perspectives. "
            f"This may not represent the full range of cultural interpretations. "
            f"Consider exploring multiple lenses for a more complete understanding."
        )
