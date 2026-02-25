"""
Cultural Interpretation Agent - CORE INNOVATION
Adapts explanations to different cultural lenses
"""


class CulturalAgent:
    def __init__(self):
        # Cultural lens database
        self.interpretations = {
            "taj_mahal": {
                "local": {
                    "perspective": "Local Indian Community",
                    "emphasis": "National pride, craftsmanship legacy, tourism impact",
                    "narrative": "The Taj Mahal represents the pinnacle of Indian craftsmanship and Mughal heritage. For many Indians, it's a symbol of national identity and artistic achievement. Local communities balance pride in this monument with concerns about over-tourism and preservation. The artisans' descendants still live in Agra, maintaining traditional marble inlay techniques passed down through generations.",
                    "emotional_context": "Pride, reverence, cultural ownership"
                },
                "asian": {
                    "perspective": "Broader Asian Context",
                    "emphasis": "Ancestry, legacy, architectural fusion, Islamic art",
                    "narrative": "The Taj Mahal exemplifies the synthesis of Persian, Islamic, and Indian architectural traditions. It represents the cultural exchange along the Silk Road and the spread of Islamic art across Asia. The emphasis on symmetry, calligraphy, and geometric patterns reflects broader Asian aesthetic principles. Many Asian visitors see it as part of a shared heritage of monumental architecture.",
                    "emotional_context": "Cultural connection, artistic appreciation, shared heritage"
                },
                "european": {
                    "perspective": "European Architectural Lens",
                    "emphasis": "Symmetry, Renaissance parallels, romantic symbolism",
                    "narrative": "European observers often emphasize the Taj Mahal's perfect symmetry and mathematical precision, drawing parallels to Renaissance ideals. The monument gained fame in Europe during the colonial period, often romanticized as an 'exotic' love story. Modern European perspectives appreciate it as a masterpiece of world architecture, though historical accounts were filtered through colonial narratives.",
                    "emotional_context": "Aesthetic admiration, romantic idealization, architectural study"
                },
                "indigenous": {
                    "perspective": "Pre-Mughal Indigenous Context",
                    "emphasis": "Land history, displaced communities, pre-Islamic traditions",
                    "narrative": "Before the Mughal period, this region had Hindu and Buddhist heritage. Some perspectives highlight how Mughal construction transformed the landscape and displaced existing communities. Indigenous architectural traditions influenced Mughal design, though this synthesis is often overlooked in dominant narratives.",
                    "emotional_context": "Historical complexity, cultural layering, contested memory"
                }
            },
            "colosseum": {
                "local": {
                    "perspective": "Roman/Italian Community",
                    "emphasis": "Ancient Roman glory, modern identity, preservation challenges",
                    "narrative": "For Romans, the Colosseum is a powerful symbol of their city's ancient grandeur and engineering prowess. It represents both pride in Roman civilization and reflection on its complexities—including the violence and slavery that built it. Modern Romans balance tourism revenue with preservation needs and the challenge of living among ancient ruins.",
                    "emotional_context": "Pride, historical weight, ambivalence about imperial past"
                },
                "european": {
                    "perspective": "European Classical Heritage",
                    "emphasis": "Foundation of Western civilization, architectural influence",
                    "narrative": "The Colosseum is seen as foundational to European identity and Western architectural tradition. It influenced countless European structures and represents the classical heritage that Renaissance and Enlightenment thinkers revered. Many European educational systems teach Roman history as the root of European culture.",
                    "emotional_context": "Cultural foundation, educational reverence, architectural inspiration"
                },
                "asian": {
                    "perspective": "Asian Historical Parallel",
                    "emphasis": "Comparative empire studies, different entertainment traditions",
                    "narrative": "Asian perspectives often compare the Colosseum to their own imperial monuments—the Great Wall, Angkor Wat, or Forbidden City. The gladiatorial spectacles contrast with Asian entertainment traditions. Some see it as representing a different path of empire-building, with lessons about power, spectacle, and decline.",
                    "emotional_context": "Comparative analysis, cultural difference, imperial reflection"
                }
            },
            "great_wall": {
                "local": {
                    "perspective": "Chinese National Identity",
                    "emphasis": "National symbol, unity, sacrifice, resilience",
                    "narrative": "The Great Wall is deeply embedded in Chinese national consciousness as a symbol of unity, perseverance, and defensive strength. It represents the sacrifices of countless workers and the determination to protect Chinese civilization. Modern Chinese see it as proof of their ancestors' ingenuity and a reminder of historical threats.",
                    "emotional_context": "National pride, historical sacrifice, cultural resilience"
                },
                "asian": {
                    "perspective": "Regional Asian Context",
                    "emphasis": "Border dynamics, cultural exchange, Silk Road",
                    "narrative": "From a broader Asian perspective, the Great Wall represents the complex relationship between settled agricultural societies and nomadic peoples. It was both a barrier and a point of exchange along the Silk Road. The wall's history reflects centuries of interaction, conflict, and trade across Asian cultures.",
                    "emotional_context": "Historical complexity, cultural interaction, border consciousness"
                },
                "european": {
                    "perspective": "European Fascination",
                    "emphasis": "Engineering marvel, exotic wonder, scale",
                    "narrative": "Europeans have long been fascinated by the Great Wall as an engineering achievement and symbol of Chinese civilization. Often exoticized in Western media, it represents the 'mysterious East' in popular imagination. Modern European perspectives appreciate it as a UNESCO site and tourist destination, though understanding of its complex history varies.",
                    "emotional_context": "Wonder, exoticism, engineering admiration"
                }
            }
        }
    
    def interpret(self, object_id: str, lens: str, facts: dict) -> dict:
        """Generate culturally adaptive interpretation"""
        if lens == "neutral":
            return {
                "perspective": "Academic/Neutral",
                "narrative": facts.get("summary", "No interpretation available"),
                "emotional_context": "Objective analysis"
            }
        
        interpretations = self.interpretations.get(object_id, {})
        interpretation = interpretations.get(lens)
        
        if not interpretation:
            return {
                "perspective": f"{lens.title()} Perspective",
                "narrative": "Interpretation not yet available for this cultural lens.",
                "emotional_context": "Pending community input"
            }
        
        return interpretation
    
    def get_available_lenses(self, object_id: str) -> list:
        """Get available cultural lenses for an object"""
        if object_id in self.interpretations:
            return list(self.interpretations[object_id].keys())
        return ["neutral"]
