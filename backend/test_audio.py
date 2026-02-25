"""
Quick test script for audio feature
"""
import os
from dotenv import load_dotenv
from agents.audio_agent import AudioAgent

load_dotenv()

def test_audio():
    print("🎧 Testing Audio Feature")
    print("=" * 50)
    
    # Check API key
    api_key = os.getenv('ELEVENLABS_API_KEY')
    if not api_key or api_key == 'your_elevenlabs_api_key_here':
        print("❌ ELEVENLABS_API_KEY not set in .env file")
        return
    
    print(f"✅ API Key found: {api_key[:20]}...")
    
    # Initialize agent
    agent = AudioAgent()
    print(f"✅ Audio Agent initialized")
    print(f"✅ Supported languages: {', '.join(agent.get_available_languages()[:5])}...")
    
    # Test text generation
    intro_text = agent.generate_landmark_intro("Taj Mahal", "India")
    print(f"\n📝 Sample intro text:")
    print(f"   {intro_text}")
    
    # Test audio generation (small text)
    print(f"\n🔊 Testing audio generation...")
    test_text = "Welcome to CultureLens. This is a test of the audio narration feature."
    
    audio_data = agent.text_to_speech(test_text, 'en')
    
    if audio_data:
        print(f"✅ Audio generated successfully!")
        print(f"   Size: {len(audio_data)} bytes")
        print(f"   Format: MP3")
        
        # Save test file
        with open('test_audio.mp3', 'wb') as f:
            f.write(audio_data)
        print(f"✅ Saved to test_audio.mp3")
        print(f"\n🎉 Audio feature is working!")
        print(f"\nYou can play test_audio.mp3 to hear the test audio.")
    else:
        print(f"❌ Failed to generate audio")
        print(f"   Check your API key and internet connection")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    test_audio()
