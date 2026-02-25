import React, { useState } from 'react';
import './Camera.css';

function Camera({ navigateTo }) {
  const [isProcessing, setIsProcessing] = useState(false);

  const handleCapture = () => {
    setIsProcessing(true);
    
    // Simulate edge AI processing
    setTimeout(() => {
      const mockLandmarks = ['taj_mahal', 'colosseum', 'great_wall'];
      const recognized = mockLandmarks[Math.floor(Math.random() * mockLandmarks.length)];
      
      navigateTo('result', { objectId: recognized, lens: 'neutral' });
    }, 1500);
  };

  return (
    <div className="camera-container">
      <div className="camera-view">
        <div className="camera-overlay">
          <p className="instruction">
            Point camera at a monument or artwork
          </p>
          <div className="camera-frame"></div>
          <p className="demo-note">
            📸 Demo Mode: Click capture to simulate recognition
          </p>
        </div>
      </div>

      <div className="camera-controls">
        <button
          className={`capture-button ${isProcessing ? 'processing' : ''}`}
          onClick={handleCapture}
          disabled={isProcessing}
        >
          {isProcessing ? '🔍 Analyzing...' : '📸 Capture'}
        </button>
        
        <button
          className="back-button"
          onClick={() => navigateTo('home')}
        >
          ← Back
        </button>
      </div>
    </div>
  );
}

export default Camera;
