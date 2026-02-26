import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import './Map.css';
import { landmarkCoordinates } from '../data/landmarkCoordinates';

// Fix for default marker icons
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
});

function Map({ navigateTo }) {
  const mapRef = useRef(null);
  const mapInstanceRef = useRef(null);
  const markersRef = useRef([]);

  useEffect(() => {
    // Only initialize if we don't have a map instance and the ref is ready
    if (mapInstanceRef.current || !mapRef.current) {
      return;
    }

    console.log('Initializing map...');

    // Create map
    const map = L.map(mapRef.current, {
      center: [20, 0],
      zoom: 2,
      minZoom: 2,
      maxZoom: 18,
      worldCopyJump: true
    });

    // Add tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 19
    }).addTo(map);

    console.log('Tile layer added');

    // Custom red icon
    const redIcon = L.icon({
      iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
      shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      shadowSize: [41, 41]
    });

    // Add markers for each landmark
    landmarkCoordinates.forEach((landmark) => {
      console.log('Adding marker for:', landmark.name);
      const marker = L.marker([landmark.lat, landmark.lon], { icon: redIcon })
        .addTo(map);

      // Create popup content
      const popupContent = `
        <div style="text-align: center; padding: 10px;">
          <h3 style="margin: 0 0 8px 0; color: #667eea; font-size: 1.2rem;">${landmark.name}</h3>
          <p style="margin: 0 0 12px 0; color: #666; font-size: 0.95rem;">${landmark.country}</p>
          <button 
            id="explore-${landmark.id}" 
            style="
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              color: white;
              border: none;
              padding: 8px 20px;
              border-radius: 20px;
              font-size: 14px;
              cursor: pointer;
              font-weight: 500;
            "
          >
            Explore
          </button>
        </div>
      `;

      marker.bindPopup(popupContent);

      // Add click handler for explore button
      marker.on('popupopen', () => {
        const button = document.getElementById(`explore-${landmark.id}`);
        if (button) {
          button.onclick = () => {
            navigateTo('result', { 
              objectId: landmark.id, 
              lens: 'local',
              detectedName: landmark.name,
              location: landmark.country
            });
          };
        }
      });

      markersRef.current.push(marker);
    });

    mapInstanceRef.current = map;
    console.log('Map initialized successfully!', map);

    // Cleanup function - only runs when component unmounts
    return () => {
      console.log('Component unmounting, cleaning up map');
      if (mapInstanceRef.current) {
        mapInstanceRef.current.remove();
        mapInstanceRef.current = null;
      }
      markersRef.current = [];
    };
  }, []); // Empty dependency array - only run once

  return (
    <div className="map-container">
      <div className="map-header">
        <button className="back-to-home" onClick={() => navigateTo('home')}>
          ← Back to Home
        </button>
        <h1 className="map-title">Explore World Heritage</h1>
        <p className="map-subtitle">Click on any marker to discover its cultural perspectives</p>
      </div>

      <div className="leaflet-map-wrapper">
        <div ref={mapRef} id="leaflet-map-container" style={{ height: '100%', width: '100%' }} />
      </div>

      <div className="map-legend">
        <div className="legend-item">
          <div className="legend-pin"></div>
          <span>{landmarkCoordinates.length} World Heritage Sites</span>
        </div>
      </div>
    </div>
  );
}

export default Map;
