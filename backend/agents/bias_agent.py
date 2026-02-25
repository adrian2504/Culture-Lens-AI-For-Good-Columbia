"""
Bias & Ethics Agent - AI for Good Signal
Provides transparency about source dominance and missing perspectives
"""


class BiasAgent:
    def __init__(self):
        # Bias analysis database
        self.bias_data = {
            "taj_mahal": {
                "source_dominance": {
                    "colonial_era": 0.45,
                    "indian_academic": 0.35,
                    "local_oral": 0.10,
                    "international": 0.10
                },
                "missing_perspectives": [
                    "Artisan families and their economic conditions",
                    "Environmental impact of marble quarrying",
                    "Perspectives of displaced communities during construction"
                ],
                "power_imbalances": [
                    "Most English-language sources reflect colonial-era British interpretations",
                    "Romantic narratives often overshadow labor and economic realities",
                    "Limited documentation of worker experiences"
                ],
                "representation_gaps": {
                    "women": "Mumtaz Mahal's own voice and agency rarely centered",
                    "workers": "Minimal documentation of artisan perspectives",
                    "local_communities": "Contemporary community voices underrepresented"
                }
            },
            "colosseum": {
                "source_dominance": {
                    "roman_elite": 0.50,
                    "european_academic": 0.35,
                    "archaeological": 0.15
                },
                "missing_perspectives": [
                    "Enslaved people who built and maintained it",
                    "Gladiators' own accounts",
                    "Non-Roman visitors' perspectives"
                ],
                "power_imbalances": [
                    "Historical records written by Roman elite, not common people",
                    "Glorification of Roman 'civilization' often ignores violence and slavery",
                    "Limited non-European interpretations in mainstream sources"
                ],
                "representation_gaps": {
                    "enslaved_people": "Voices of those who built it largely absent",
                    "gladiators": "Mostly portrayed through elite Roman lens",
                    "victims": "Those who died in spectacles rarely memorialized"
                }
            },
            "great_wall": {
                "source_dominance": {
                    "chinese_official": 0.50,
                    "western_academic": 0.30,
                    "archaeological": 0.20
                },
                "missing_perspectives": [
                    "Nomadic peoples on the other side of the wall",
                    "Forced laborers who died during construction",
                    "Border communities' daily experiences"
                ],
                "power_imbalances": [
                    "Narratives dominated by imperial Chinese perspective",
                    "Western sources often exoticize or oversimplify",
                    "Nomadic peoples' perspectives rarely included"
                ],
                "representation_gaps": {
                    "workers": "Millions died building it, few records of their lives",
                    "nomadic_peoples": "Often portrayed as 'barbarians' rather than complex societies",
                    "border_communities": "Daily life along the wall underexplored"
                }
            }
        }
    
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
