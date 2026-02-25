# CultureLens - Quick Start Guide

## 🚀 Start in 30 Seconds

### Terminal 1 - Backend
```bash
cd backend
source venv/bin/activate
python main.py
```

### Terminal 2 - Webapp
```bash
cd webapp
npm start
```

### Browser
Opens automatically at: http://localhost:3000

## 🎯 Try These Features

### 1. Interactive Map (30 seconds)
```
Home → "Explore Map" → Click any pin → View perspectives
```

### 2. Audio Narration (1 minute)
```
Map → Click Taj Mahal → Scroll to audio player → 
Select Hindi 🇮🇳 → Click "Listen" → Enjoy!
```

### 3. Image Upload (1 minute)
```
Home → "Scan Landmark" → "Upload Image" → 
Select landmark photo → View AI analysis
```

### 4. Camera Capture (1 minute)
```
Home → "Scan Landmark" → "Capture Live" → 
Grant permission → Capture → View results
```

## ✨ Key Features

- 🗺️ **Interactive Map**: 13 world heritage sites
- 🎧 **Audio Narration**: 10 languages
- 🌍 **Cultural Lenses**: 4 perspectives
- 🤖 **AI Recognition**: GPT-4o Vision
- ⚖️ **Bias Transparency**: Shows missing voices
- 💬 **Community Sentiment**: Visitor reflections

## 🔑 API Keys Configured

- ✅ OpenAI (GPT-4o): For vision & text
- ✅ ElevenLabs: For audio narration

## 📊 Status

- ✅ Backend: Port 8000
- ✅ Webapp: Port 3000
- ✅ All agents: Working
- ✅ Audio: Ready
- ✅ Map: Interactive

## 🎨 Demo Flow

### Best Demo Path:
1. **Start**: "Explore Map" button
2. **Hover**: See landmark info cards
3. **Click**: Taj Mahal pin
4. **View**: Cultural perspectives
5. **Switch**: Try different lenses
6. **Listen**: Select Hindi, click "Listen"
7. **Explore**: Try other landmarks

### Wow Moments:
- 🗺️ Beautiful world map with pulse animations
- 🎧 Natural audio in 10 languages
- 🌍 4 different cultural perspectives
- ⚖️ Bias transparency section
- 💬 Community sentiment display

## 💡 Quick Tips

- **Map not showing?** Hard refresh (Ctrl+Shift+R)
- **Audio not playing?** Check backend is running
- **Slow first load?** Normal, AI is generating
- **Want to test?** Use diagnostic tools in `/public`

## 📁 Important Files

```
backend/
├── main.py              # API server
├── agents/              # All AI agents
│   ├── vision_agent.py
│   ├── audio_agent.py
│   └── ...
└── .env                 # API keys

webapp/
├── src/
│   ├── pages/
│   │   ├── Map.js       # Interactive map
│   │   └── Result.js    # Cultural perspectives
│   └── components/
│       └── AudioPlayer.js  # Audio feature
```

## 🐛 Troubleshooting

### Backend won't start?
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Webapp won't start?
```bash
cd webapp
npm install
npm start
```

### Audio not working?
```bash
cd backend
python test_audio.py  # Test audio feature
```

## 📚 Documentation

- **Full README**: `README.md`
- **Audio Setup**: `AUDIO_FEATURE_SETUP.md`
- **Audio Ready**: `AUDIO_READY.md`
- **Map Guide**: `MAP_FEATURE_GUIDE.md`
- **Testing**: `TESTING_CHECKLIST.md`

## 🎉 You're Ready!

Everything is set up and working. Just start both servers and explore!

**Enjoy CultureLens!** 🌍✨
