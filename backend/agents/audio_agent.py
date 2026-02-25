"""
Audio Agent - Handles text-to-speech with translation using ElevenLabs + OpenAI
"""
import os
import requests
from typing import Optional, Dict
import json
from elevenlabs.client import ElevenLabs
from io import BytesIO
import time
from openai import OpenAI

class AudioAgent:
    def __init__(self):
        self.api_key = os.getenv('ELEVENLABS_API_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.base_url = "https://api.elevenlabs.io/v1"
        
        # Initialize clients
        if self.api_key:
            self.client = ElevenLabs(api_key=self.api_key)
        else:
            self.client = None
            
        if self.openai_key:
            self.openai_client = OpenAI(api_key=self.openai_key)
        else:
            self.openai_client = None
        
        # Language codes and names
        self.supported_languages = {
            'english': {'code': 'en', 'name': 'English'},
            'spanish': {'code': 'es', 'name': 'Spanish'},
            'hindi': {'code': 'hi', 'name': 'Hindi'},
            'italian': {'code': 'it', 'name': 'Italian'},
            'french': {'code': 'fr', 'name': 'French'},
            'german': {'code': 'de', 'name': 'German'},
            'portuguese': {'code': 'pt', 'name': 'Portuguese'},
            'chinese': {'code': 'zh', 'name': 'Chinese'},
            'japanese': {'code': 'ja', 'name': 'Japanese'},
            'arabic': {'code': 'ar', 'name': 'Arabic'}
        }
        
        # Voice IDs for multilingual TTS
        self.voice_ids = {
            'en': 'EXAVITQu4vr4xnSDxMaL',  # Sarah - English
            'es': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'hi': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'it': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'fr': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'de': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'pt': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'zh': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'ja': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
            'ar': 'EXAVITQu4vr4xnSDxMaL',  # Use multilingual voice
        }
    
    def translate_text(self, text: str, target_language: str) -> str:
        """
        Translate text to target language using OpenAI
        """
        if not self.openai_client or target_language == 'en':
            return text
        
        try:
            lang_name = self.supported_languages.get(target_language, {}).get('name', target_language)
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f"You are a professional translator. Translate the following text to {lang_name}. Only return the translation, nothing else."},
                    {"role": "user", "content": text}
                ],
                temperature=0.3
            )
            
            translated = response.choices[0].message.content.strip()
            print(f"✅ Translated to {lang_name}: {translated[:100]}...")
            return translated
            
        except Exception as e:
            print(f"Translation error: {e}")
            return text  # Return original if translation fails
    
    def text_to_speech_multilingual(self, text: str, target_language: str = 'en') -> Optional[bytes]:
        """
        Convert text to speech with translation
        1. Translate text to target language (using OpenAI)
        2. Generate speech in that language (using ElevenLabs multilingual voice)
        """
        if not self.client:
            print("Warning: ELEVENLABS_API_KEY not set")
            return None
        
        try:
            # Step 1: Translate text if not English
            if target_language != 'en':
                print(f"Translating to {target_language}...")
                text = self.translate_text(text, target_language)
            
            # Step 2: Generate speech using multilingual voice
            voice_id = self.voice_ids.get(target_language, self.voice_ids['en'])
            
            url = f"{self.base_url}/text-to-speech/{voice_id}"
            
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.api_key
            }
            
            # Use eleven_multilingual_v2 model
            data = {
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "style": 0.0,
                    "use_speaker_boost": True
                }
            }
            
            print(f"Generating speech...")
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                print(f"✅ Audio generated: {len(response.content)} bytes")
                return response.content
            else:
                print(f"TTS Error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Error in multilingual TTS: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def generate_landmark_intro(self, landmark_name: str, country: str) -> str:
        """
        Generate introduction text for a landmark
        """
        return f"This is the {landmark_name}, located in {country}. Would you like to hear more about it in a specific language?"
    
    def generate_narration(self, landmark_data: Dict, language: str = 'english') -> str:
        """
        Generate narration text from landmark data
        """
        facts = landmark_data.get('facts', {})
        interpretation = landmark_data.get('interpretation', {})
        
        # Create a narrative combining facts and interpretation
        narration = f"{facts.get('name', 'This landmark')} is located in {facts.get('location', 'an amazing place')}. "
        narration += f"It was built in {facts.get('built', 'ancient times')}. "
        
        if interpretation.get('narrative'):
            narration += interpretation['narrative']
        
        return narration
    
    def get_language_options_text(self, landmark_name: str) -> str:
        """
        Generate text offering language options
        """
        languages = ", ".join([lang.capitalize() for lang in list(self.supported_languages.keys())[:5]])
        return f"I can tell you about {landmark_name} in {languages}, or other languages. Which would you prefer?"
    
    def create_audio_response(self, text: str, language: str = 'english') -> Optional[bytes]:
        """
        Create audio response for given text and language
        Uses translation + multilingual TTS
        """
        lang_code = self.supported_languages.get(language.lower(), {}).get('code', 'en')
        return self.text_to_speech_multilingual(text, lang_code)
    
    def get_available_languages(self) -> list:
        """
        Get list of supported languages
        """
        return list(self.supported_languages.keys())
