import React, { useState, useRef } from 'react';
import './AudioPlayer.css';

const API_URL = 'http://localhost:8000';

function AudioPlayer({ objectId, culturalLens }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('english');
  const [showLanguages, setShowLanguages] = useState(false);
  const [loading, setLoading] = useState(false);
  const audioRef = useRef(null);

  const languages = [
    { code: 'english', name: 'English', flag: '🇬🇧' },
    { code: 'spanish', name: 'Spanish', flag: '🇪🇸' },
    { code: 'hindi', name: 'Hindi', flag: '🇮🇳' },
    { code: 'italian', name: 'Italian', flag: '🇮🇹' },
    { code: 'french', name: 'French', flag: '🇫🇷' },
    { code: 'german', name: 'German', flag: '🇩🇪' },
    { code: 'portuguese', name: 'Portuguese', flag: '🇵🇹' },
    { code: 'chinese', name: 'Chinese', flag: '🇨🇳' },
    { code: 'japanese', name: 'Japanese', flag: '🇯🇵' },
    { code: 'arabic', name: 'Arabic', flag: '🇸🇦' }
  ];

  const playAudio = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/audio/narrate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          object_id: objectId,
          language: selectedLanguage,
          cultural_lens: culturalLens
        })
      });

      if (response.ok) {
        const audioBlob = await response.blob();
        const audioUrl = URL.createObjectURL(audioBlob);
        
        if (audioRef.current) {
          audioRef.current.src = audioUrl;
          audioRef.current.play();
          setIsPlaying(true);
        }
      } else {
        console.error('Failed to generate audio');
        alert('Audio generation failed. Make sure ELEVENLABS_API_KEY is set in backend/.env');
      }
    } catch (error) {
      console.error('Error playing audio:', error);
      alert('Failed to connect to audio service');
    } finally {
      setLoading(false);
    }
  };

  const stopAudio = () => {
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
      setIsPlaying(false);
    }
  };

  const handleLanguageSelect = (langCode) => {
    setSelectedLanguage(langCode);
    setShowLanguages(false);
    if (isPlaying) {
      stopAudio();
    }
  };

  const selectedLang = languages.find(l => l.code === selectedLanguage);

  return (
    <div className="audio-player">
      <audio
        ref={audioRef}
        onEnded={() => setIsPlaying(false)}
        onPause={() => setIsPlaying(false)}
      />

      <div className="audio-controls">
        <div className="language-selector">
          <button 
            className="language-button"
            onClick={() => setShowLanguages(!showLanguages)}
          >
            <span className="flag">{selectedLang?.flag}</span>
            <span className="lang-name">{selectedLang?.name}</span>
            <span className="dropdown-arrow">{showLanguages ? '▲' : '▼'}</span>
          </button>

          {showLanguages && (
            <div className="language-dropdown">
              {languages.map((lang) => (
                <button
                  key={lang.code}
                  className={`language-option ${selectedLanguage === lang.code ? 'active' : ''}`}
                  onClick={() => handleLanguageSelect(lang.code)}
                >
                  <span className="flag">{lang.flag}</span>
                  <span>{lang.name}</span>
                </button>
              ))}
            </div>
          )}
        </div>

        <button
          className={`play-button ${isPlaying ? 'playing' : ''}`}
          onClick={isPlaying ? stopAudio : playAudio}
          disabled={loading}
        >
          {loading ? (
            <>
              <span className="spinner"></span>
              <span>Generating...</span>
            </>
          ) : isPlaying ? (
            <>
              <span className="icon">⏸</span>
              <span>Pause</span>
            </>
          ) : (
            <>
              <span className="icon">🔊</span>
              <span>Listen</span>
            </>
          )}
        </button>
      </div>

      <div className="audio-info">
        <p>🎧 Hear this perspective in {selectedLang?.name}</p>
      </div>
    </div>
  );
}

export default AudioPlayer;
