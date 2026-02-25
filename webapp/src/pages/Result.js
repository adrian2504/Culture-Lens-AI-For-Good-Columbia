import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Result.css';

const API_URL = 'http://localhost:8000';

function Result({ navigateTo, landmark }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [currentLens, setCurrentLens] = useState(landmark?.lens || 'neutral');
  const [error, setError] = useState(null);

  useEffect(() => {
    if (landmark) {
      fetchInterpretation();
    }
  }, [currentLens, landmark]);

  const fetchInterpretation = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${API_URL}/interpret`, {
        object_id: landmark.objectId,
        cultural_lens: currentLens,
        user_context: {
          detected_name: landmark.detectedName,
          location: landmark.location
        }
      });
      setData(response.data);
    } catch (err) {
      setError('Failed to connect to backend. Make sure it\'s running on port 8000.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="result-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading cultural insights...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="result-container">
        <div className="error">
          <h2>❌ Connection Error</h2>
          <p>{error}</p>
          <button onClick={() => navigateTo('home')}>← Back to Home</button>
        </div>
      </div>
    );
  }

  if (!data) return null;

  return (
    <div className="result-container">
      <div className="result-header">
        <h1>{data.facts.name}</h1>
        <p className="location">📍 {data.facts.location}</p>
      </div>

      {/* Cultural Lens Selector */}
      <div className="lens-selector">
        <h3>Choose Cultural Lens:</h3>
        <div className="lens-buttons">
          {['neutral', ...data.available_lenses].map((lens) => (
            <button
              key={lens}
              className={`lens-button ${currentLens === lens ? 'active' : ''}`}
              onClick={() => setCurrentLens(lens)}
            >
              {lens.charAt(0).toUpperCase() + lens.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Interpretation */}
      <div className="section interpretation-section">
        <h2>{data.interpretation.perspective}</h2>
        <p className="narrative">{data.interpretation.narrative}</p>
        <p className="emotion">💭 {data.interpretation.emotional_context}</p>
      </div>

      {/* Facts */}
      <div className="section facts-section">
        <h2>Historical Facts</h2>
        <div className="fact">📅 Built: {data.facts.built}</div>
        <div className="fact">👤 Builder: {data.facts.builder}</div>
        <div className="fact">🎨 Style: {data.facts.style}</div>
        <div className="fact">🏗️ Material: {data.facts.material}</div>
      </div>

      {/* Community Sentiment */}
      {data.community_sentiment && data.community_sentiment.reflections_count > 0 && (
        <div className="section community-section">
          <h2>💬 Community Perspectives</h2>
          <p className="community-count">
            {data.community_sentiment.reflections_count} people have shared their perspectives
          </p>
          
          {data.community_sentiment.emotions && Object.keys(data.community_sentiment.emotions).length > 0 && (
            <>
              <h3>Emotional Responses:</h3>
              <div className="emotion-bars">
                {Object.entries(data.community_sentiment.emotions).map(([emotion, value]) => (
                  <div key={emotion} className="emotion-bar">
                    <span className="emotion-label">{emotion}</span>
                    <div className="emotion-bar-container">
                      <div className="emotion-bar-fill" style={{ width: `${value * 100}%` }}></div>
                    </div>
                    <span className="emotion-percent">{Math.round(value * 100)}%</span>
                  </div>
                ))}
              </div>
            </>
          )}

          {data.community_sentiment.common_themes && data.community_sentiment.common_themes.length > 0 && (
            <>
              <h3>Common Themes:</h3>
              <div className="themes-list">
                {data.community_sentiment.common_themes.map((theme, idx) => (
                  <div key={idx} className="theme-tag">{theme}</div>
                ))}
              </div>
            </>
          )}

          {data.community_sentiment.sample_quotes && data.community_sentiment.sample_quotes.length > 0 && (
            <>
              <h3>Visitor Reflections:</h3>
              {data.community_sentiment.sample_quotes.map((quote, idx) => (
                <div key={idx} className="quote-card">
                  <span className="quote-icon">"</span>
                  <p>{quote}</p>
                </div>
              ))}
            </>
          )}
        </div>
      )}

      {/* Bias Report */}
      {data.bias_report && (
        <div className="section bias-section">
          <h2>⚖️ Bias Transparency</h2>
          {data.bias_report.transparency_note && (
            <p className="bias-note">{data.bias_report.transparency_note}</p>
          )}
          
          {data.bias_report.source_dominance && (
            <>
              <h3>Source Distribution:</h3>
              {Object.entries(data.bias_report.source_dominance).map(([source, percent]) => (
                <div key={source} className="source-bar">
                  <span className="source-label">{source.replace('_', ' ')}</span>
                  <div className="bar-container">
                    <div className="bar" style={{ width: `${percent * 100}%` }}></div>
                  </div>
                  <span className="source-percent">{Math.round(percent * 100)}%</span>
                </div>
              ))}
            </>
          )}

          {data.bias_report.missing_perspectives && data.bias_report.missing_perspectives.length > 0 && (
            <>
              <h3>Missing Perspectives:</h3>
              <ul className="missing-list">
                {data.bias_report.missing_perspectives.map((perspective, idx) => (
                  <li key={idx}>{perspective}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}

      <button className="home-button" onClick={() => navigateTo('home')}>
        ← Back to Home
      </button>
    </div>
  );
}

export default Result;
