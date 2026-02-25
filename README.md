# CultureLens 🌍

**AI-powered, culturally adaptive guide for art, monuments, and heritage**

## One-Line Pitch
CultureLens uses edge AI and culturally adaptive agents to help people understand art and heritage through many perspectives—not just one.

## Problem
Most cultural guides present a single "official" narrative, often reflecting Western or colonial bias. This leads to cultural erasure and shallow understanding.

## Solution
Multi-agent AI system that provides:
- **Edge Vision Agent**: On-device image recognition (privacy-first)
- **Knowledge Agent**: Verified historical facts
- **Cultural Interpretation Agent**: Adaptive explanations across cultural lenses
- **Community Sentiment Agent**: Aggregated lived experiences
- **Bias & Ethics Agent**: Source transparency and missing perspectives

## Tech Stack
- **Mobile**: React Native + Expo
- **Edge AI**: TensorFlow Lite / MobileNet
- **Backend**: FastAPI + Python
- **Agent System**: LangGraph-style orchestration
- **Vector DB**: FAISS (local) or Pinecone

## Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Mobile
```bash
cd mobile
npm install
npx expo start
```

## MVP Scope
- 5 famous landmarks (Taj Mahal, Colosseum, Great Wall, Statue of Liberty, Pyramids)
- 3 cultural lenses each (Local, Asian, European)
- Edge image recognition
- Mock community data
- Bias transparency layer

## AI for Good Alignment
✅ Cultural preservation  
✅ Diversity & inclusion  
✅ Accessibility (offline support)  
✅ Bias transparency  
✅ Human-in-the-loop AI
