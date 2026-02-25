# CultureLens - Quick Start Guide

## Prerequisites
- Python 3.8+ 
- Node.js 16+
- npm or yarn

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

# Install Python dependencies
pip3 install -r requirements.txt

# Start the API server
python3 main.py
```

You should see:
```
✓ Using Hardcoded Cultural Agent (fast demo mode)
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

## Step 3: Start the Mobile App (3 minutes)

Open a **new terminal** (keep backend running):

```bash
# Navigate to mobile folder
cd mobile

# Install dependencies
npm install

# Start Expo
npx expo start
```

You'll see a QR code and options:
- Press `w` - Open in web browser (easiest)
- Press `i` - Open iOS simulator (requires Xcode)
- Press `a` - Open Android emulator (requires Android Studio)

---

## Step 4: Use the App

### Quick Demo (No Camera Needed)
1. Click **"🧪 Demo: Taj Mahal"**
2. Switch between cultural lenses (Local, Asian, European, Indigenous)
3. Scroll down to see bias transparency

### Camera Demo
1. Click **"📷 Scan Monument"**
2. Grant camera permission
3. Point at anything and click "📸 Capture"
4. View the interpretation

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

### Mobile Issues

**"npm: command not found"**
- Install Node.js from https://nodejs.org

**"Cannot connect to backend"**

If testing on a physical device, update the API URL:

1. Find your computer's IP:
```bash
# macOS/Linux
ifconfig | grep "inet " | grep -v 127.0.0.1
```

2. Edit `mobile/app/result.tsx` line 7:
```typescript
const API_URL = 'http://YOUR_IP_HERE:8000';
// Example: const API_URL = 'http://192.168.1.100:8000';
```

**Expo won't start**
```bash
# Clear cache
npx expo start -c
```

---

## Project Structure

```
culturelens/
├── backend/              # FastAPI server
│   ├── main.py          # API endpoints
│   ├── agents/          # AI agent modules
│   └── requirements.txt
├── mobile/              # React Native app
│   ├── app/            # Expo Router pages
│   └── package.json
└── README.md
```

---

## What's Running?

- **Backend**: http://localhost:8000 (API server)
- **Mobile**: http://localhost:8081 (Expo dev server)
- **Web App**: Opens automatically in browser when you press `w`

---

## Next Steps

1. ✅ Run the demo
2. 📖 Read `DEMO.md` for presentation tips
3. 🤖 Check `LLM_SETUP.md` to enable AI-powered interpretations
4. 🎨 Customize cultural lenses in `backend/agents/cultural_agent.py`

---

## Quick Commands Reference

```bash
# Start backend
cd backend && python3 main.py

# Start mobile (new terminal)
cd mobile && npx expo start

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
- Mobile not starting? Check Node version: `node --version` (need 16+)
- Can't connect? Make sure backend is running first
- Still stuck? Check the full error message and search for it

---

## Demo Tips

1. Start with the **"🧪 Demo: Taj Mahal"** button (no camera needed)
2. Show lens switching to demonstrate multiple perspectives
3. Highlight the **bias transparency section** (AI for Good)
4. Explain edge AI concept (camera processing stays on-device)
5. Mention scalability (easy to add new landmarks and lenses)

Good luck! 🚀
