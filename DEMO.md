# CultureLens Demo Guide

## Quick Start (5 Minutes)

### 1. Start Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Backend runs on `http://localhost:8000`

### 2. Test API (Optional)
```bash
# Test cultural interpretation
curl -X POST http://localhost:8000/interpret \
  -H "Content-Type: application/json" \
  -d '{"object_id": "taj_mahal", "cultural_lens": "local"}'
```

### 3. Start Mobile App
```bash
cd mobile
npm install
npx expo start
```
Press `w` for web, `i` for iOS simulator, or `a` for Android

## Demo Flow

### Option 1: Quick Demo (No Camera)
1. Open app
2. Click "🧪 Demo: Taj Mahal"
3. Switch between cultural lenses
4. Observe bias transparency section

### Option 2: Camera Demo
1. Click "📷 Scan Monument"
2. Grant camera permission
3. Point at any object (mock recognition)
4. View multi-perspective interpretation

## Key Features to Highlight

### 1. Cultural Lens Switching
- Start with "Neutral" (academic facts)
- Switch to "Local" (Indian community perspective)
- Try "Asian" (regional context)
- Compare "European" (Western lens)

### 2. Bias Transparency
- Source dominance visualization
- Missing perspectives listed
- Power imbalances highlighted
- Diversity score calculated

### 3. Edge AI Concept
- Camera processing happens "on-device"
- No raw images uploaded (privacy)
- Fast recognition
- Works offline (in production)

## API Endpoints

### GET /
Health check

### POST /analyze/image
Simulates edge vision (in production: on-device)
```json
{
  "object_id": "taj_mahal",
  "confidence": 0.92,
  "visual_tags": ["mughal", "islamic", "marble"],
  "processing": "edge"
}
```

### POST /interpret
Multi-agent cultural interpretation
```json
{
  "object_id": "taj_mahal",
  "cultural_lens": "local",
  "user_context": {}
}
```

### GET /lenses
Available cultural perspectives

## Available Landmarks

1. **taj_mahal** - 4 lenses (local, asian, european, indigenous)
2. **colosseum** - 3 lenses (local, european, asian)
3. **great_wall** - 3 lenses (local, asian, european)
4. **statue_liberty** - Coming soon
5. **pyramids_giza** - Coming soon

## Judge Talking Points

### Innovation
- Multi-agent architecture (vision → knowledge → cultural → bias)
- Cultural lens switching (not just one narrative)
- Bias transparency layer (AI for Good)

### Technical
- Edge AI for privacy (TensorFlow Lite concept)
- Modular agent design (easy to extend)
- RESTful API (scalable)

### Impact
- Cultural preservation
- Bias awareness
- Inclusive education
- Accessibility (offline capable)

### Scalability
- Add new landmarks: Just update knowledge DB
- Add new lenses: Extend cultural agent
- Community contributions: Future crowdsourcing
- Multi-language: i18n ready

## Troubleshooting

### Backend won't start
```bash
# Check Python version (3.8+)
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Mobile app issues
```bash
# Clear cache
npx expo start -c

# Check Node version (16+)
node --version
```

### API connection failed
- Update `API_URL` in `mobile/app/result.tsx`
- Use your machine's IP instead of localhost for physical devices
- Example: `http://192.168.1.100:8000`

## Next Steps (Post-Hackathon)

1. **Real Edge AI**: Integrate TensorFlow Lite with trained model
2. **LLM Integration**: Use Mistral/LLaMA for dynamic interpretations
3. **Community Platform**: User-contributed perspectives
4. **AR Overlay**: Real-time camera annotations
5. **Audio Guide**: Text-to-speech for accessibility
6. **Offline Mode**: Cache interpretations locally
7. **More Landmarks**: Expand to 100+ sites
8. **Sentiment Analysis**: Aggregate emotional responses
