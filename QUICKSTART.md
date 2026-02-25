# CultureLens - Quick Start Guide

## Prerequisites
- Python 3.8+ 
- Node.js 16+
- npm or yarn
- OpenAI API key

Check versions:
```bash
python3 --version
node --version
npm --version
```

---

## Step 1: Start the Backend (2 minutes)

```bash
# Navigate to backend folder
cd backend

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Add your OpenAI API key to .env file
# The .env file should already exist with the key configured

# Start the API server
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal open!** The backend needs to stay running.

---

## Step 2: Test Backend (Optional)

Open a new terminal and test:
```bash
curl http://localhost:8000
```

Should return: `{"message":"CultureLens API","status":"running"}`

---

## Step 3: Start the Web App (2 minutes)

Open a **new terminal** (keep backend running):

```bash
# Navigate to webapp folder
cd webapp

# Install dependencies (first time only)
npm install

# Start the development server
npm start
```

The app will automatically open in your browser at http://localhost:3000

---

## Step 4: Use the App

### Option 1: Explore the Interactive Map
1. Click **"Explore Map"** on the home page
2. Hover over red pins to see landmark details
3. Click any pin to view its cultural perspectives
4. Switch between cultural lenses (Local, Asian, European, Indigenous)

### Option 2: Scan a Landmark
1. Click **"Scan Landmark"** on the home page
2. Choose **"Upload Image"** or **"Capture Live"**
3. Upload a photo of a famous landmark
4. View AI-powered recognition and cultural interpretations
5. Explore bias transparency and community insights

---

## Troubleshooting

### Backend Issues

**"pip3: command not found"**
```bash
# Try just 'pip'
pip install -r requirements.txt
```

**"python3: command not found"**
```bash
# Try just 'python'
python main.py
```

**Port 8000 already in use**
```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9

# Or change port in main.py (last line):
# uvicorn.run(app, host="0.0.0.0", port=8001)
```

**Missing OpenAI API key**
- Make sure `.env` file exists in the backend folder
- Check that `OPENAI_API_KEY` is set correctly

### Web App Issues

**"npm: command not found"**
- Install Node.js from https://nodejs.org

**"Cannot connect to backend"**
- Make sure the backend is running on port 8000
- Check that you see "Uvicorn running" in the backend terminal
- Try accessing http://localhost:8000 in your browser

**Port 3000 already in use**
```bash
# The app will ask if you want to use a different port
# Press 'y' to use port 3001 instead
```

**Video background not showing**
- Copy your video file to `webapp/public/video/Culture Lens.mp4`
- The video should be named exactly "Culture Lens.mp4"

---

## Project Structure

```
culturelens/
├── backend/              # FastAPI server
│   ├── main.py          # API endpoints
│   ├── agents/          # AI agent modules
│   ├── data/            # JSON data files
│   ├── .env             # OpenAI API key
│   └── requirements.txt
├── webapp/              # React web app
│   ├── src/
│   │   ├── pages/      # Home, Camera, Map, Result
│   │   └── App.js
│   ├── public/
│   │   └── video/      # Background video
│   └── package.json
└── README.md
```

---

## What's Running?

- **Backend**: http://localhost:8000 (API server)
- **Web App**: http://localhost:3000 (React dev server)

---

## Next Steps

1. ✅ Run the app and explore the interactive map
2. 📖 Read `DEMO.md` for presentation tips
3. 🎨 Customize cultural lenses in `backend/agents/llm_cultural_agent.py`
4. 📊 Check `IMPLEMENTATION_STATUS.md` to see what's implemented

---

## Quick Commands Reference

```bash
# Start backend
cd backend && source venv/bin/activate && python main.py

# Start webapp (new terminal)
cd webapp && npm start

# Test API
curl http://localhost:8000/interpret \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"object_id":"taj_mahal","cultural_lens":"local"}'

# Stop everything
# Press Ctrl+C in both terminals
```

---

## Need Help?

- Backend not starting? Check Python version: `python3 --version` (need 3.8+)
- Web app not starting? Check Node version: `node --version` (need 16+)
- Can't connect? Make sure backend is running first
- Still stuck? Check the full error message

---

## Demo Tips

1. Start with the **"Explore Map"** to show the interactive world heritage map
2. Click on different landmarks to demonstrate instant access
3. Switch between cultural lenses to show multiple perspectives
4. Highlight the **bias transparency section** (AI for Good)
5. Show the **community sentiment** feature
6. Try uploading a real landmark photo to demonstrate AI recognition

Good luck! 🚀
