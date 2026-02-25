// Accurate coordinates for world heritage landmarks
export const landmarkCoordinates = [
  { id: 'taj_mahal', name: 'Taj Mahal', country: 'India', lat: 27.1751, lon: 78.0421 },
  { id: 'eiffel_tower', name: 'Eiffel Tower', country: 'France', lat: 48.8584, lon: 2.2945 },
  { id: 'statue_liberty', name: 'Statue of Liberty', country: 'USA', lat: 40.6892, lon: -74.0445 },
  { id: 'colosseum', name: 'Colosseum', country: 'Italy', lat: 41.8902, lon: 12.4922 },
  { id: 'great_wall', name: 'Great Wall', country: 'China', lat: 40.4319, lon: 116.5704 },
  { id: 'pyramids_giza', name: 'Pyramids of Giza', country: 'Egypt', lat: 29.9792, lon: 31.1342 },
  { id: 'machu_picchu', name: 'Machu Picchu', country: 'Peru', lat: -13.1631, lon: -72.5450 },
  { id: 'christ_redeemer', name: 'Christ the Redeemer', country: 'Brazil', lat: -22.9519, lon: -43.2105 },
  { id: 'big_ben', name: 'Big Ben', country: 'UK', lat: 51.5007, lon: -0.1246 },
  { id: 'stonehenge', name: 'Stonehenge', country: 'UK', lat: 51.1789, lon: -1.8262 },
  { id: 'acropolis', name: 'Acropolis', country: 'Greece', lat: 37.9715, lon: 23.7267 },
  { id: 'petra', name: 'Petra', country: 'Jordan', lat: 30.3285, lon: 35.4444 },
  { id: 'angkor_wat', name: 'Angkor Wat', country: 'Cambodia', lat: 13.4125, lon: 103.8670 }
];

// Convert lat/lon to SVG coordinates (for 100x60 viewBox)
// Mercator projection simplified
export function latLonToSVG(lat, lon) {
  // Normalize longitude: -180 to 180 → 0 to 100
  const x = ((lon + 180) / 360) * 100;
  
  // Normalize latitude: 85 to -85 → 0 to 60 (Mercator projection limits)
  // Invert because SVG y increases downward
  const y = ((85 - lat) / 170) * 60;
  
  return { x, y };
}

// Get SVG coordinates for all landmarks
export function getLandmarksWithSVGCoords() {
  return landmarkCoordinates.map(landmark => {
    const svgCoords = latLonToSVG(landmark.lat, landmark.lon);
    return {
      ...landmark,
      x: svgCoords.x,
      y: svgCoords.y
    };
  });
}
