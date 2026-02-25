#!/bin/bash

# CultureLens Audio Feature Setup Script

echo "🎧 CultureLens Audio Feature Setup"
echo "=================================="
echo ""

# Check if we're in the right directory
if [ ! -d "backend" ]; then
    echo "❌ Error: Please run this script from the CultureLens root directory"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "backend/venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    cd backend
    python3 -m venv venv
    cd ..
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source backend/venv/bin/activate

# Install elevenlabs package
echo "📥 Installing elevenlabs package..."
pip install elevenlabs==1.0.0

# Check if .env exists
if [ ! -f "backend/.env" ]; then
    echo "❌ Error: backend/.env file not found"
    exit 1
fi

# Check if ELEVENLABS_API_KEY is set
if grep -q "ELEVENLABS_API_KEY=your_elevenlabs_api_key_here" backend/.env; then
    echo ""
    echo "⚠️  ELEVENLABS_API_KEY not configured!"
    echo ""
    echo "To complete setup:"
    echo "1. Go to https://elevenlabs.io/ and sign up"
    echo "2. Get your API key from the dashboard"
    echo "3. Edit backend/.env and replace 'your_elevenlabs_api_key_here' with your actual key"
    echo ""
    read -p "Do you have your API key ready? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your ElevenLabs API key: " api_key
        # Update .env file
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            sed -i '' "s/ELEVENLABS_API_KEY=your_elevenlabs_api_key_here/ELEVENLABS_API_KEY=$api_key/" backend/.env
        else
            # Linux
            sed -i "s/ELEVENLABS_API_KEY=your_elevenlabs_api_key_here/ELEVENLABS_API_KEY=$api_key/" backend/.env
        fi
        echo "✅ API key saved to backend/.env"
    else
        echo "⏭️  Skipping API key setup. You can add it manually later."
    fi
else
    echo "✅ ELEVENLABS_API_KEY already configured"
fi

echo ""
echo "✅ Audio feature setup complete!"
echo ""
echo "Next steps:"
echo "1. Start backend: cd backend && python main.py"
echo "2. Start webapp: cd webapp && npm start"
echo "3. Navigate to any landmark and try the audio feature!"
echo ""
echo "📚 For more info, see AUDIO_FEATURE_SETUP.md"
