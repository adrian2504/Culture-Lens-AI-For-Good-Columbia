import React from 'react';
import './Home.css';

function Home({ navigateTo }) {
  return (
    <div className="home-container">
      <div className="home-content">
        <h1 className="title">🌍 CultureLens</h1>
        <p className="subtitle">
          Discover art and heritage through multiple cultural perspectives
        </p>

        <button
          className="primary-button"
          onClick={() => navigateTo('camera')}
        >
          📷 Scan Monument
        </button>

        <button
          className="secondary-button"
          onClick={() => navigateTo('result', { objectId: 'taj_mahal', lens: 'local' })}
        >
          🧪 Demo: Taj Mahal
        </button>

        <div className="features">
          <div className="feature">✓ Edge AI (Privacy-First)</div>
          <div className="feature">✓ Multiple Cultural Lenses</div>
          <div className="feature">✓ Bias Transparency</div>
          <div className="feature">✓ Community Perspectives</div>
        </div>
      </div>
    </div>
  );
}

export default Home;
