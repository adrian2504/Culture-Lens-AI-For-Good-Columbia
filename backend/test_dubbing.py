"""
Test dubbing functionality
"""
import os
from dotenv import load_dotenv
from agents.audio_agent import AudioAgent

load_dotenv()

def test_dubbing():
    print("🎧 Testing Dubbing Feature")
    print("=" * 60)
    
    agent = AudioAgent()
    
    # Test text
    test_text = "The Taj Mahal is a beautiful monument in India."
    
    print(f"\n📝 Test text: {test_text}")
    print(f"\n🔊 Generating audio in Hindi...")
    print(f"   This will take 5-10 seconds...")
    
    # Generate dubbed audio
    audio_data = agent.create_audio_response(test_text, 'hindi')
    
    if audio_data:
        print(f"\n✅ Audio generated successfully!")
        print(f"   Size: {len(audio_data)} bytes")
        
        # Save file
        with open('test_hindi_dubbed.mp3', 'wb') as f:
            f.write(audio_data)
        print(f"✅ Saved to test_hindi_dubbed.mp3")
        print(f"\n🎉 Dubbing is working!")
        print(f"\nPlay the file to hear Hindi audio:")
        print(f"   open test_hindi_dubbed.mp3")
    else:
        print(f"\n❌ Failed to generate dubbed audio")
        print(f"   Check the error messages above")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_dubbing()
