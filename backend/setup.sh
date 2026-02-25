#!/bin/bash
# CultureLens Backend Setup Script

echo "🌍 Setting up CultureLens backend..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To start the backend:"
echo "  source venv/bin/activate"
echo "  python main.py"
