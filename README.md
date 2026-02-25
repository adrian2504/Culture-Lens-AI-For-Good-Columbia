# CultureLens 🌍

**AI-powered, culturally adaptive guide for art, monuments, and heritage**

## One-Line Pitch
CultureLens uses AI vision and culturally adaptive agents to help people understand art and heritage through many perspectives—not just one.

## Problem
Most cultural guides present a single "official" narrative, often reflecting Western or colonial bias. This leads to cultural erasure and shallow understanding.

## Solution
Multi-agent AI system that provides:
- **Vision Agent**: Real image recognition using OpenAI Vision API
- **Knowledge Agent**: Verified historical facts
- **Cultural Interpretation Agent**: AI-generated adaptive explanations across cultural lenses
- **Bias & Ethics Agent**: Source transparency and missing perspectives

## Features
- 📸 Upload or capture photos of landmarks
- 🤖 AI-powered landmark recognition
- 🗺️ Interactive world map with 13 heritage sites
- 🌍 Multiple cultural perspectives (Local, Asian, European, Indigenous)
- ⚖️ Bias transparency with source analysis
- 💬 Community sentiment and visitor reflections
- 🎧 Audio narration in 10 languages (powered by ElevenLabs)
- 🎨 Beautiful, responsive web interface with video background

## Tech Stack
- **Frontend**: React web app
- **Backend**: FastAPI + Python
- **AI**: OpenAI GPT-4o-mini (Vision + Text)
- **Agent System**: Modular Python architecture

## Quick Start

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Add your OpenAI API key to .env
echo "USE_LLM=true" > .env
echo "LLM_PROVIDER=openai" >> .env
echo "OPENAI_API_KEY=your-key-here" >> .env

python main.py
```

### 2. Web App Setup
```bash
cd webapp
npm install
npm start
```

Open http://localhost:3000

## Supported Landmarks
- Taj Mahal
- Colosseum
- Great Wall of China
- Statue of Liberty
- Pyramids of Giza
- Eiffel Tower
- Big Ben
- Christ the Redeemer
- Machu Picchu
- Petra
- Angkor Wat
- Stonehenge
- Acropolis

## How It Works

### Option 1: Scan a Landmark
1. **Upload/Capture**: User uploads or captures a photo of a landmark
2. **Vision Recognition**: OpenAI Vision API identifies the landmark
3. **Knowledge Retrieval**: System fetches verified historical facts
4. **Cultural Interpretation**: AI generates perspective-specific narratives
5. **Bias Analysis**: System shows source distribution and missing perspectives
6. **Community Insights**: View aggregated visitor sentiments and reflections
7. **User Exploration**: User can switch between different cultural lenses

### Option 2: Explore the Map
1. **Interactive Map**: Browse 13 world heritage sites on an interactive map
2. **Hover & Click**: Hover over pins to see landmark details, click to explore
3. **Instant Access**: Jump directly to any landmark's cultural perspectives

## AI for Good Alignment
✅ Cultural preservation  
✅ Diversity & inclusion  
✅ Bias transparency  
✅ Accessible education  
✅ Respectful AI

## Cost
- Image recognition: ~$0.003 per image
- Cultural interpretation: ~$0.0001 per lens
- Total per lookup: ~$0.004 (very affordable)
