# CultureLens Demo Guide

## Quick Start (5 Minutes)

### 1. Start Backend
```bash
cd backend
source venv/bin/activate  # Activate virtual environment
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

### 3. Start Web App
```bash
cd webapp
npm install  # First time only
npm start
```
Opens automatically at `http://localhost:3000`

## Demo Flow

### Option 1: Interactive Map (Recommended Start) ✨
1. Open app at http://localhost:3000
2. Click "Explore Map" button
3. Hover over red pins to see landmark details
4. Click on "Taj Mahal" pin
5. View all cultural perspectives
6. Switch between 4 cultural lenses
7. Scroll to see bias transparency and community sentiment

### Option 2: Image Upload
1. Click "Scan Landmark" button
2. Click "Upload Image"
3. Upload a photo of a famous landmark (Statue of Liberty, Eiffel Tower, etc.)
4. AI recognizes the landmark using GPT-4o Vision
5. View multi-perspective interpretation
6. Explore all sections

### Option 3: Live Camera Capture
1. Click "Scan Landmark" button
2. Click "Capture Live"
3. Grant camera permission
4. See live video feed
5. Click "Capture Photo"
6. View AI-powered recognition and interpretation

## Key Features to Highlight

### 1. Interactive World Map ✨ NEW!
- 13 world heritage sites with red pins
- Hover to see landmark details
- Click to explore cultural perspectives
- Beautiful animations and transitions
- Instant access to any landmark

### 2. AI-Powered Recognition
- Real GPT-4o Vision API integration
- Upload photos or capture live
- Accurate landmark identification
- Confidence scoring
- Works with 13+ famous landmarks

### 3. Cultural Lens Switching
- Start with "Local" (community perspective)
- Switch to "Asian" (regional context)
- Try "European" (Western lens)
- Compare "Indigenous" (traditional knowledge)
- AI-generated narratives using GPT-4o-mini

### 4. Bias Transparency (AI for Good)
- Source dominance visualization
- Missing perspectives listed
- Power imbalances highlighted
- Representation gaps identified
- Diversity score calculated

### 5. Community Sentiment
- Aggregated emotional responses
- Common themes from visitors
- Authentic quotes and reflections
- Reflection count display

## API Endpoints

### GET /
Health check - Returns API status

### POST /analyze/image
Vision recognition using GPT-4o
- Accepts base64 encoded image
- Returns landmark identification
- Includes confidence score
- Provides visual tags

### POST /interpret
Multi-agent cultural interpretation
```json
{
  "object_id": "taj_mahal",
  "cultural_lens": "local"
}
```
Returns:
- Historical facts (Knowledge Agent)
- Cultural narrative (Cultural Agent)
- Bias analysis (Bias Agent)
- Community sentiment (Community Agent)

### GET /lenses
Available cultural perspectives: local, asian, european, indigenous

## Available Landmarks (13 Total)

1. **taj_mahal** - Taj Mahal, India
2. **eiffel_tower** - Eiffel Tower, France
3. **statue_liberty** - Statue of Liberty, USA
4. **colosseum** - Colosseum, Italy
5. **great_wall** - Great Wall, China
6. **pyramids_giza** - Pyramids of Giza, Egypt
7. **machu_picchu** - Machu Picchu, Peru
8. **christ_redeemer** - Christ the Redeemer, Brazil
9. **big_ben** - Big Ben, UK
10. **stonehenge** - Stonehenge, UK
11. **acropolis** - Acropolis, Greece
12. **petra** - Petra, Jordan
13. **angkor_wat** - Angkor Wat, Cambodia

All landmarks have 4 cultural lenses with AI-generated interpretations!

## Judge Talking Points

### Innovation
- **Multi-agent architecture**: Vision → Knowledge → Cultural → Bias → Community
- **Cultural lens switching**: 4 different perspectives, not just one narrative
- **Bias transparency layer**: Shows what's missing, not just what's there (AI for Good)
- **Interactive map**: Visual exploration of world heritage
- **AI-powered recognition**: Real GPT-4o Vision integration

### Technical Excellence
- **Modern tech stack**: React, FastAPI, OpenAI GPT-4o
- **Modular agent design**: Easy to extend and maintain
- **RESTful API**: Scalable architecture
- **Real AI integration**: Not mocked, actual GPT-4o Vision and text generation
- **Beautiful UI**: Video background, animations, glassmorphism

### Impact (AI for Good)
- **Cultural preservation**: Multiple perspectives prevent erasure
- **Bias awareness**: Transparent about missing voices
- **Inclusive education**: Accessible to all backgrounds
- **Community-driven**: Aggregates visitor sentiments
- **Respectful AI**: Acknowledges power imbalances

### Scalability
- **Add landmarks**: Just update JSON database
- **Add lenses**: Extend cultural agent prompts
- **Add languages**: i18n ready architecture
- **Community contributions**: Future crowdsourcing platform
- **Cost-effective**: ~$0.004 per lookup

### Demo Highlights
1. **Start with map**: "We have 13 world heritage sites you can explore visually"
2. **Click a pin**: "Each landmark has 4 different cultural interpretations"
3. **Switch lenses**: "Notice how the narrative completely changes"
4. **Show bias section**: "We're transparent about whose voices are missing"
5. **Show community**: "Real visitor sentiments add emotional context"
6. **Upload photo**: "You can also upload your own photos for AI recognition"

## Troubleshooting

### Backend Issues

**Backend won't start**
```bash
# Check Python version (3.8+)
python --version

# Activate virtual environment
source backend/venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**OpenAI API errors**
- Check `.env` file has valid `OPENAI_API_KEY`
- Verify API key has credits
- Test with: `curl https://api.openai.com/v1/models -H "Authorization: Bearer YOUR_KEY"`

**Port 8000 in use**
```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9
```

### Web App Issues

**App won't start**
```bash
# Check Node version (16+)
node --version

# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm start
```

**Cannot connect to backend**
- Ensure backend is running on port 8000
- Check http://localhost:8000 in browser
- Look for CORS errors in browser console

**Video background not showing**
- Copy video file to `webapp/public/video/Culture Lens.mp4`
- Check file name is exactly "Culture Lens.mp4"
- Video is optional, app works without it

**Camera not working**
- Grant camera permission in browser
- Use HTTPS or localhost (required for camera access)
- Check browser supports getUserMedia API

### Common Errors

**"Module not found"**
- Run `pip install -r requirements.txt` in backend
- Run `npm install` in webapp

**"Connection refused"**
- Start backend first, then webapp
- Check both are running in separate terminals

**"Invalid API key"**
- Verify OpenAI API key in `backend/.env`
- Check key format: `sk-proj-...`

## Next Steps (Post-Demo)

### Immediate Enhancements
1. **More landmarks**: Expand to 50+ sites
2. **User accounts**: Save favorites and history
3. **Audio narration**: Text-to-speech for accessibility
4. **Mobile app**: React Native version for app stores
5. **Offline mode**: Cache interpretations locally

### Advanced Features
1. **User contributions**: Community-submitted perspectives
2. **AR overlay**: Real-time camera annotations
3. **Social sharing**: Share discoveries on social media
4. **Gamification**: Badges for exploring landmarks
5. **Multi-language**: Support 10+ languages

### Technical Improvements
1. **Edge AI**: TensorFlow Lite for on-device recognition
2. **Vector DB**: FAISS/Pinecone for semantic search
3. **Caching**: Redis for faster responses
4. **Analytics**: Track user engagement
5. **A/B testing**: Optimize user experience

### Scaling
1. **CDN**: Serve static assets globally
2. **Load balancing**: Handle more traffic
3. **Database**: PostgreSQL for user data
4. **Monitoring**: Error tracking and performance
5. **CI/CD**: Automated deployment

## Cost Analysis

### Current (Per Lookup)
- Image recognition (GPT-4o): ~$0.003
- 4 cultural interpretations (GPT-4o-mini): ~$0.0004
- **Total: ~$0.004 per complete lookup**

### At Scale (1000 users/day)
- Daily cost: ~$4
- Monthly cost: ~$120
- Very affordable for a production app!

## Resources

### Documentation
- `README.md` - Project overview
- `QUICKSTART.md` - Setup guide
- `IMPLEMENTATION_STATUS.md` - Feature checklist
- `PROJECT_SUMMARY.md` - Complete summary
- `MAP_FEATURE_GUIDE.md` - Map documentation
- `TESTING_CHECKLIST.md` - QA checklist

### Code Structure
- `backend/agents/` - All AI agents
- `backend/data/` - JSON databases
- `webapp/src/pages/` - All UI pages
- `webapp/src/App.js` - Main router

Good luck with your demo! 🚀
