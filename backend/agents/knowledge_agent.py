"""
Knowledge Retrieval Agent
Fetches verified historical facts from neutral sources
"""


class KnowledgeAgent:
    def __init__(self):
        # Mock knowledge base (in production: Wikipedia API, Wikidata, museum APIs)
        self.knowledge_db = {
            "taj_mahal": {
                "name": "Taj Mahal",
                "location": "Agra, India",
                "built": "1632-1653",
                "builder": "Mughal Emperor Shah Jahan",
                "purpose": "Mausoleum for wife Mumtaz Mahal",
                "style": "Mughal architecture (Islamic, Persian, Indian fusion)",
                "material": "White marble, precious stones",
                "unesco": True,
                "sources": ["UNESCO", "Archaeological Survey of India", "Wikipedia"]
            },
            "colosseum": {
                "name": "Colosseum",
                "location": "Rome, Italy",
                "built": "70-80 CE",
                "builder": "Emperor Vespasian, completed by Titus",
                "purpose": "Amphitheater for gladiatorial contests and public spectacles",
                "style": "Roman architecture",
                "material": "Concrete, stone, tuff",
                "unesco": True,
                "sources": ["UNESCO", "Italian Ministry of Culture", "Wikipedia"]
            },
            "great_wall": {
                "name": "Great Wall of China",
                "location": "Northern China",
                "built": "7th century BCE - 17th century CE",
                "builder": "Multiple Chinese dynasties",
                "purpose": "Military defense, border control",
                "style": "Chinese defensive architecture",
                "material": "Stone, brick, tamped earth, wood",
                "unesco": True,
                "sources": ["UNESCO", "China National Cultural Heritage Administration", "Wikipedia"]
            },
            "statue_liberty": {
                "name": "Statue of Liberty",
                "location": "New York Harbor, USA",
                "built": "1875-1886",
                "builder": "Frédéric Auguste Bartholdi (sculptor), Gustave Eiffel (structure)",
                "purpose": "Gift from France, symbol of freedom and democracy",
                "style": "Neoclassical",
                "material": "Copper sheets over iron framework",
                "unesco": True,
                "sources": ["UNESCO", "National Park Service", "Wikipedia"]
            },
            "pyramids_giza": {
                "name": "Pyramids of Giza",
                "location": "Giza, Egypt",
                "built": "c. 2580-2560 BCE (Great Pyramid)",
                "builder": "Pharaoh Khufu (Great Pyramid)",
                "purpose": "Royal tombs",
                "style": "Ancient Egyptian architecture",
                "material": "Limestone, granite",
                "unesco": True,
                "sources": ["UNESCO", "Egyptian Ministry of Tourism and Antiquities", "Wikipedia"]
            }
        }
    
    def get_facts(self, object_id: str) -> dict:
        """Retrieve neutral, verified facts"""
        facts = self.knowledge_db.get(object_id)
        if not facts:
            return {"error": "No knowledge available for this object"}
        
        # Add neutral summary
        facts["summary"] = self._generate_neutral_summary(facts)
        return facts
    
    def _generate_neutral_summary(self, facts: dict) -> str:
        """Generate factual summary"""
        return (
            f"The {facts['name']} is located in {facts['location']}. "
            f"Built between {facts['built']}, it was constructed by {facts['builder']} "
            f"as a {facts['purpose']}. The structure exemplifies {facts['style']} "
            f"and is primarily made of {facts['material']}."
        )
