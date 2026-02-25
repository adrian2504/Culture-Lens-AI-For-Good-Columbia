# Audio Narration Feature - Setup Guide

## 🎧 Overview

CultureLens now includes interactive audio narration powered by ElevenLabs! Users can:
1. Select from 10 languages (English, Spanish, Hindi, Italian, French, German, Portuguese, Chinese, Japanese, Arabic)
2. Listen to cultural perspectives in their chosen language
3. Get AI-generated, natural-sounding narration

## 🔑 Get ElevenLabs API Key

### Step 1: Sign Up
1. Go to https://elevenlabs.io/
2. Click "Sign Up" (free tier available)
3. Verify your email

### Step 2: Get API Key
1. Log in to your dashboard
2. Click on your profile (top right)
3. Select "Profile + API Key"
4. Copy your API key

### Step 3: Add to Environment
```bash
# Edit backend/.env
cd backend
nano .env  # or use your preferred editor
```

Add this line:
```
ELEVENLABS_API_KEY=your_actual_api_key_here
```

## 📦 Install Dependencies

```bash
cd backend
source venv/bin/activate  # Activate virtual environment
pip install elevenlabs==1.0.0
```

## 🚀 How It Works

### User Flow:
1. User views a landmark (e.g., Taj Mahal)
2. Selects a cultural lens (Local, Asian, European, Indigenous)
3. Clicks language dropdown (shows flag + language name)
4. Selects desired language (e.g., Hindi 🇮🇳)
5. Clicks "Listen" button
6. Audio is generated and plays automatically

### Technical Flow:
```
Frontend (AudioPlayer.js)
    ↓
POST /audio/narrate
    ↓
Audio Agent (audio_agent.py)
    ↓
ElevenLabs API
    ↓
MP3 Audio Stream
    ↓
Browser Audio Player
```

## 🎨 Features

### Language Support
- **English** 🇬🇧 - Default
- **Spanish** 🇪🇸 - For Latin American audiences
- **Hindi** 🇮🇳 - For Indian landmarks
- **Italian** 🇮🇹 - For European heritage
- **French** 🇫🇷 - For French-speaking regions
- **German** 🇩🇪 - For German-speaking regions
- **Portuguese** 🇵🇹 - For Brazilian/Portuguese sites
- **Chinese** 🇨🇳 - For Asian audiences
- **Japanese** 🇯🇵 - For Japanese heritage
- **Arabic** 🇸🇦 - For Middle Eastern sites

### Audio Quality
- Natural-sounding voices
- Multilingual support
- Proper pronunciation
- Emotional tone matching

## 🧪 Testing

### Test Without API Key (Mock Mode)
If you don't have an API key yet, the system will:
- Return the text that would be narrated
- Show an error message
- Still display the UI

### Test With API Key
1. Start backend: `python backend/main.py`
2. Start webapp: `npm start` in webapp folder
3. Navigate to any landmark
4. Click language dropdown
5. Select a language
6. Click "Listen"
7. Audio should play within 3-5 seconds

## 💰 Cost

### ElevenLabs Pricing (as of 2024):
- **Free Tier**: 10,000 characters/month
- **Starter**: $5/month - 30,000 characters
- **Creator**: $22/month - 100,000 characters

### Estimated Usage:
- Average narration: ~500 characters
- Free tier: ~20 narrations/month
- Starter tier: ~60 narrations/month

### Cost Per Narration:
- ~$0.001 - $0.005 per narration
- Very affordable for demos and small-scale use

## 🔧 API Endpoints

### GET /audio/languages
Returns available languages
```json
{
  "languages": ["english", "spanish", "hindi", ...]
}
```

### POST /audio/intro
Generate introduction audio
```json
{
  "object_id": "taj_mahal",
  "language": "hindi"
}
```

Returns: MP3 audio stream

### POST /audio/narrate
Generate full narration audio
```json
{
  "object_id": "taj_mahal",
  "language": "hindi",
  "cultural_lens": "local"
}
```

Returns: MP3 audio stream

## 🎯 UI Components

### AudioPlayer Component
Location: `webapp/src/components/AudioPlayer.js`

Features:
- Language dropdown with flags
- Play/Pause button
- Loading spinner
- Error handling
- Auto-stop on language change

### Styling
Location: `webapp/src/components/AudioPlayer.css`

Design:
- Glassmorphism effect
- Purple gradient theme
- Smooth animations
- Responsive layout
- Flag emojis for visual appeal

## 🐛 Troubleshooting

### Audio Not Playing
1. **Check API Key**: Verify `ELEVENLABS_API_KEY` in `backend/.env`
2. **Check Backend**: Ensure backend is running on port 8000
3. **Check Console**: Look for errors in browser console (F12)
4. **Check Network**: Look for failed requests in Network tab

### "Failed to generate audio"
- API key is missing or invalid
- ElevenLabs API is down
- Rate limit exceeded (free tier)
- Network connectivity issue

### Audio Quality Issues
- Check internet connection
- Try different language/voice
- Verify text content is clean

### Language Not Working
- Some languages may not be available in free tier
- Check ElevenLabs documentation for supported languages
- Try English as fallback

## 📝 Code Structure

```
backend/
├── agents/
│   └── audio_agent.py          # Audio generation logic
├── main.py                     # Audio endpoints
└── .env                        # API key here

webapp/
├── src/
│   ├── components/
│   │   ├── AudioPlayer.js      # Audio UI component
│   │   └── AudioPlayer.css     # Audio styling
│   └── pages/
│       └── Result.js           # Integrated audio player
```

## 🚀 Future Enhancements

### Planned Features:
1. **Voice Selection**: Let users choose different voices
2. **Speed Control**: Adjust playback speed
3. **Download Audio**: Save narrations for offline use
4. **Caching**: Cache generated audio to reduce API calls
5. **Transcript**: Show text while audio plays
6. **Auto-play**: Option to auto-play on page load
7. **Playlist**: Queue multiple landmarks
8. **Background Music**: Add ambient sounds

### Advanced Features:
1. **Voice Cloning**: Custom voices for specific cultures
2. **Emotion Control**: Adjust tone based on content
3. **Sound Effects**: Add ambient sounds (temple bells, etc.)
4. **3D Audio**: Spatial audio for immersive experience

## ✅ Checklist

Before using audio feature:
- [ ] ElevenLabs account created
- [ ] API key obtained
- [ ] API key added to `backend/.env`
- [ ] `elevenlabs` package installed
- [ ] Backend restarted
- [ ] Webapp refreshed
- [ ] Test audio playback
- [ ] Check all languages work
- [ ] Verify error handling

## 📚 Resources

- [ElevenLabs Documentation](https://elevenlabs.io/docs)
- [ElevenLabs API Reference](https://elevenlabs.io/docs/api-reference)
- [Voice Library](https://elevenlabs.io/voice-library)
- [Pricing](https://elevenlabs.io/pricing)

## 🎉 Success!

If you can:
1. See the audio player on Result page
2. Select different languages
3. Click "Listen" and hear audio
4. Switch languages and hear different voices

Then the audio feature is working perfectly! 🎊

---

**Note**: The audio feature is optional. The app works fine without it, but it adds a great accessibility and engagement feature!
