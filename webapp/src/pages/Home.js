import React, { useRef, useEffect } from 'react';
import './Home.css';

function Home({ navigateTo }) {
  const videoRef = useRef(null);

  useEffect(() => {
    // Handle video autoplay with error handling
    if (videoRef.current) {
      videoRef.current.play().catch(error => {
        // Silently handle autoplay errors (common in Safari)
        console.log('Video autoplay prevented:', error.message);
      });
    }
  }, []);

  return (
    <div className="home-container">
      {/* Video Background */}
      <video 
        ref={videoRef}
        loop 
        muted 
        playsInline 
        className="video-background"
      >
        <source src="/video/Culture Lens.mp4" type="video/mp4" />
      </video>
      
      {/* Overlay */}
      <div className="video-overlay"></div>

      <div className="home-content">
        <div className="logo-section">
          <div className="brand-container">
            <h1 className="title">
              <span className="title-culture">Culture</span>
              <span className="title-lens">Lens</span>
            </h1>
            <div className="tagline">Discover Heritage Through AI</div>
          </div>
        </div>

        <p className="subtitle">
          Experience world landmarks through multiple cultural perspectives
        </p>

        <div className="button-group">
          <button
            className="primary-button"
            onClick={() => navigateTo('camera')}
          >
            <span className="button-text">Scan Landmark</span>
            <div className="button-shine"></div>
          </button>

          <button
            className="secondary-button"
            onClick={() => navigateTo('map')}
          >
            <span className="button-text">Explore Map</span>
          </button>
        </div>

        <div className="features">
          <div className="feature-card">
            <div className="feature-icon">🤖</div>
            <div className="feature-text">AI Recognition</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🌏</div>
            <div className="feature-text">Cultural Perspectives</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚖️</div>
            <div className="feature-text">Bias Transparency</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">💬</div>
            <div className="feature-text">Community Insights</div>
          </div>
        </div>

        <div className="landmark-showcase">
          <div className="showcase-title">Explore World Heritage</div>
          <div className="landmark-grid">
            <div className="landmark-item">Eiffel Tower</div>
            <div className="landmark-item">Statue of Liberty</div>
            <div className="landmark-item">Taj Mahal</div>
            <div className="landmark-item">Colosseum</div>
            <div className="landmark-item">Great Wall</div>
            <div className="landmark-item">Machu Picchu</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
