import React, { useState } from 'react';
import './Map.css';
import { getLandmarksWithSVGCoords } from '../data/landmarkCoordinates';

function Map({ navigateTo }) {
  const [hoveredLandmark, setHoveredLandmark] = useState(null);
  
  // Get landmarks with accurate SVG coordinates based on real lat/lon
  const landmarks = getLandmarksWithSVGCoords();

  const handleLandmarkClick = (landmark) => {
    navigateTo('result', { 
      objectId: landmark.id, 
      lens: 'local',
      detectedName: landmark.name,
      location: landmark.country
    });
  };

  return (
    <div className="map-container">
      <div className="map-header">
        <button className="back-to-home" onClick={() => navigateTo('home')}>
          ← Back to Home
        </button>
        <h1 className="map-title">Explore World Heritage</h1>
        <p className="map-subtitle">Click on any landmark to discover its cultural perspectives</p>
      </div>

      {/* Info display */}
      <div className="map-info">
        {hoveredLandmark ? (
          <div className="info-content">
            <strong>{landmarks.find(l => l.id === hoveredLandmark)?.name}</strong>
            {' - '}
            {landmarks.find(l => l.id === hoveredLandmark)?.country}
          </div>
        ) : (
          <div className="info-content">Hover over a pin to see details</div>
        )}
      </div>

      <div className="world-map">
        <svg viewBox="0 0 100 60" className="map-svg">
          {/* Background */}
          <defs>
            <linearGradient id="oceanGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style={{ stopColor: '#1e3a8a', stopOpacity: 0.5 }} />
              <stop offset="100%" style={{ stopColor: '#0ea5e9', stopOpacity: 0.5 }} />
            </linearGradient>
          </defs>
          
          {/* Ocean */}
          <rect x="0" y="0" width="100" height="60" fill="url(#oceanGradient)" />
          
          {/* World Map - Simplified continents */}
          {/* North America */}
          <path d="M 15,15 Q 18,12 22,13 L 28,15 Q 30,18 29,22 L 27,28 Q 25,32 22,33 L 18,32 Q 15,30 14,26 L 13,20 Q 14,17 15,15 Z" 
                fill="#10b981" opacity="0.4" stroke="rgba(255,255,255,0.3)" strokeWidth="0.2" />
          
          {/* South America */}
          <path d="M 25,35 L 28,36 Q 30,38 31,42 L 32,48 Q 31,52 29,54 L 27,55 Q 25,54 24,52 L 23,48 Q 22,44 23,40 L 24,37 Q 25,35 25,35 Z" 
                fill="#10b981" opacity="0.4" stroke="rgba(255,255,255,0.3)" strokeWidth="0.2" />
          
          {/* Europe */}
          <path d="M 45,20 L 50,18 Q 53,19 54,22 L 55,26 Q 54,28 52,29 L 48,30 Q 46,29 45,27 L 44,23 Q 44,21 45,20 Z" 
                fill="#10b981" opacity="0.4" stroke="rgba(255,255,255,0.3)" strokeWidth="0.2" />
          
          {/* Africa */}
          <path d="M 48,32 L 52,31 Q 55,32 57,35 L 59,40 Q 60,45 58,50 L 55,53 Q 52,54 49,53 L 47,50 Q 46,45 47,40 L 48,35 Q 48,32 48,32 Z" 
                fill="#10b981" opacity="0.4" stroke="rgba(255,255,255,0.3)" strokeWidth="0.2" />
          
          {/* Asia */}
          <path d="M 56,15 L 62,13 Q 68,14 73,16 L 78,19 Q 82,22 83,26 L 84,32 Q 83,36 80,39 L 75,42 Q 70,44 65,43 L 60,41 Q 57,38 56,34 L 55,28 Q 55,22 56,18 L 56,15 Z" 
                fill="#10b981" opacity="0.4" stroke="rgba(255,255,255,0.3)" strokeWidth="0.2" />
          
          {/* Australia */}
          <path d="M 75,48 Q 78,47 81,48 L 84,50 Q 85,52 84,54 L 82,56 Q 79,57 76,56 L 74,54 Q 73,52 74,50 L 75,48 Z" 
                fill="#10b981" opacity="0.4" stroke="rgba(255,255,255,0.3)" strokeWidth="0.2" />
          
          {/* Grid lines - Equator and Prime Meridian */}
          <line x1="0" y1="30" x2="100" y2="30" stroke="rgba(255,255,255,0.4)" strokeWidth="0.15" strokeDasharray="2,1" />
          <line x1="50" y1="0" x2="50" y2="60" stroke="rgba(255,255,255,0.4)" strokeWidth="0.15" strokeDasharray="2,1" />
          
          {/* Additional latitude lines */}
          <line x1="0" y1="20" x2="100" y2="20" stroke="rgba(255,255,255,0.2)" strokeWidth="0.1" strokeDasharray="1,1" />
          <line x1="0" y1="40" x2="100" y2="40" stroke="rgba(255,255,255,0.2)" strokeWidth="0.1" strokeDasharray="1,1" />
          
          {/* Additional longitude lines */}
          <line x1="25" y1="0" x2="25" y2="60" stroke="rgba(255,255,255,0.2)" strokeWidth="0.1" strokeDasharray="1,1" />
          <line x1="75" y1="0" x2="75" y2="60" stroke="rgba(255,255,255,0.2)" strokeWidth="0.1" strokeDasharray="1,1" />
          
          {/* Landmark pins */}
          {landmarks.map((landmark) => (
            <g
              key={landmark.id}
              className="landmark-pin"
              onMouseEnter={() => setHoveredLandmark(landmark.id)}
              onMouseLeave={() => setHoveredLandmark(null)}
              onClick={() => handleLandmarkClick(landmark)}
            >
              {/* Clickable area (invisible but large) */}
              <circle 
                cx={landmark.x} 
                cy={landmark.y} 
                r="3" 
                fill="transparent" 
                style={{ cursor: 'pointer' }}
              />
              
              {/* Pin shadow */}
              <ellipse 
                cx={landmark.x} 
                cy={landmark.y + 1.8} 
                rx="1.2" 
                ry="0.5" 
                fill="rgba(0,0,0,0.5)" 
              />
              
              {/* Pin body */}
              <path
                d={`M ${landmark.x},${landmark.y - 3} 
                    C ${landmark.x - 1.5},${landmark.y - 3} ${landmark.x - 2.2},${landmark.y - 2.2} ${landmark.x - 2.2},${landmark.y - 0.8} 
                    C ${landmark.x - 2.2},${landmark.y + 0.8} ${landmark.x},${landmark.y + 3} ${landmark.x},${landmark.y + 3} 
                    C ${landmark.x},${landmark.y + 3} ${landmark.x + 2.2},${landmark.y + 0.8} ${landmark.x + 2.2},${landmark.y - 0.8} 
                    C ${landmark.x + 2.2},${landmark.y - 2.2} ${landmark.x + 1.5},${landmark.y - 3} ${landmark.x},${landmark.y - 3} Z`}
                fill={hoveredLandmark === landmark.id ? '#dc2626' : '#ef4444'}
                stroke="white"
                strokeWidth="0.25"
                style={{ cursor: 'pointer', transition: 'all 0.2s' }}
              />
              
              {/* Pin dot */}
              <circle 
                cx={landmark.x} 
                cy={landmark.y - 1.2} 
                r="0.6" 
                fill="white" 
                style={{ pointerEvents: 'none' }}
              />
              
              {/* Pulse ring */}
              {hoveredLandmark === landmark.id && (
                <circle 
                  cx={landmark.x} 
                  cy={landmark.y} 
                  r="3" 
                  fill="none" 
                  stroke="#ef4444" 
                  strokeWidth="0.2" 
                  opacity="0.6"
                  className="pulse-ring"
                  style={{ pointerEvents: 'none' }}
                />
              )}
            </g>
          ))}
        </svg>
      </div>

      <div className="map-legend">
        <div className="legend-item">
          <div className="legend-pin"></div>
          <span>{landmarks.length} World Heritage Sites</span>
        </div>
      </div>
    </div>
  );
}

export default Map;
