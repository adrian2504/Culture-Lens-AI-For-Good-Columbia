import React, { useState } from 'react';
import './App.css';
import Home from './pages/Home';
import Camera from './pages/Camera';
import Result from './pages/Result';
import Map from './pages/Map';

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [selectedLandmark, setSelectedLandmark] = useState(null);

  const navigateTo = (page, landmark = null) => {
    setCurrentPage(page);
    if (landmark) setSelectedLandmark(landmark);
  };

  return (
    <div className="App">
      {currentPage === 'home' && <Home navigateTo={navigateTo} />}
      {currentPage === 'camera' && <Camera navigateTo={navigateTo} />}
      {currentPage === 'result' && <Result navigateTo={navigateTo} landmark={selectedLandmark} />}
      {currentPage === 'map' && <Map navigateTo={navigateTo} />}
    </div>
  );
}

export default App;
