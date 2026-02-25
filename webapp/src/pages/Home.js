import React from 'react';
import './Home.css';

function Home({ navigateTo }) {
  return (
    <div className="home-container">
      {/* Animated background elements */}
      <div className="floating-landmarks">
        <div className="landmark-icon landmark-1">🗼</div>
        <div className="landmark-icon landmark-2">🗽</div>
        <div className="landmark-icon landmark-3">🕌</div>
        <div className="landmark-icon landmark-4">🏛️</div>
        <div className="landmark-icon landmark-5">🗿</div>
        <div className="landmark-icon landmark-6">⛩️</div>
      </div>

      <div className="home-content">
        <div className="logo-section">
          <div className="camera-icon">
            📷
            <div className="camera-flash"></div>
          </div>
          <h1 className="title">
            <span className="title-culture">Culture</span>
            <span className="title-lens">Lens</span>
          </h1>
          <div className="globe-icon rotating">🌍</div>
        </div>

        <p className="subtitle">
          Discover world heritage through AI-powered cultural perspectives
        </p>

        <div className="button-group">
          <button
            className="primary-button pulse"
            onClick={() => navigateTo('camera')}
          >
            <span className="button-icon">📸</span>
            <span>Recognize Landmark</span>
            <div className="button-shine"></div>
          </button>

          <button
            className="secondary-button"
            onClick={() => navigateTo('result', { objectId: 'taj_mahal', lens: 'local' })}
          >
            <span className="button-icon">✨</span>
            <span>Try Demo</span>
          </button>
        </div>

        <div className="features">
          <div className="feature-card">
            <div className="feature-icon">🤖</div>
            <div className="feature-text">AI Recognition</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🌏</div>
            <div className="feature-text">Cultural Lenses</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚖️</div>
            <div className="feature-text">Bias Transparency</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🏛️</div>
            <div className="feature-text">World Heritage</div>
          </div>
        </div>

        <div className="landmark-showcase">
          <div className="showcase-title">Explore Famous Landmarks</div>
          <div className="landmark-grid">
            <div className="landmark-item">🗼 Eiffel Tower</div>
            <div className="landmark-item">🗽 Statue of Liberty</div>
            <div className="landmark-item">🕌 Taj Mahal</div>
            <div className="landmark-item">🏛️ Colosseum</div>
            <div className="landmark-item">🏯 Great Wall</div>
            <div className="landmark-item">🗿 Machu Picchu</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
