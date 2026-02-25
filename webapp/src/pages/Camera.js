import React, { useState, useRef } from 'react';
import axios from 'axios';
import './Camera.css';

const API_URL = 'http://localhost:8000';

function Camera({ navigateTo }) {
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState(null);
  const [mode, setMode] = useState('upload'); // 'upload' or 'camera'
  const [stream, setStream] = useState(null);
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const startCamera = async () => {
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia({ 
        video: { facingMode: 'environment' } 
      });
      setStream(mediaStream);
      if (videoRef.current) {
        videoRef.current.srcObject = mediaStream;
      }
      setMode('camera');
      setError(null);
    } catch (err) {
      setError('Camera access denied. Please use upload instead.');
      console.error('Camera error:', err);
    }
  };

  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
    }
    setMode('upload');
  };

  const capturePhoto = () => {
    if (!videoRef.current || !canvasRef.current) return;
    
    const canvas = canvasRef.current;
    const video = videoRef.current;
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    
    canvas.toBlob(blob => {
      if (blob) {
        processImage(blob);
      }
    }, 'image/jpeg', 0.8);
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      processImage(file);
    }
  };

  const processImage = async (imageBlob) => {
    setIsProcessing(true);
    setError(null);
    
    try {
      const formData = new FormData();
      formData.append('file', imageBlob, 'image.jpg');
      
      const response = await axios.post(`${API_URL}/analyze/image`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      if (response.data.error) {
        setError(response.data.error);
        setIsProcessing(false);
        return;
      }
      
      // Stop camera if active
      stopCamera();
      
      // Navigate to results
      navigateTo('result', { 
        objectId: response.data.object_id,
        detectedName: response.data.detected_name,
        location: response.data.location,
        lens: 'neutral' 
      });
      
    } catch (err) {
      setError('Failed to analyze image. Please try again.');
      console.error('Processing error:', err);
      setIsProcessing(false);
    }
  };

  return (
    <div className="camera-container">
      <div className="camera-view">
        {mode === 'upload' ? (
          <div className="upload-section">
            <h2>📸 Recognize Landmark</h2>
            <p>Upload a photo or use your camera</p>
            
            <label className="upload-button">
              📁 Upload Photo
              <input 
                type="file" 
                accept="image/*" 
                onChange={handleFileUpload}
                disabled={isProcessing}
                style={{ display: 'none' }}
              />
            </label>
            
            <button 
              className="camera-button"
              onClick={startCamera}
              disabled={isProcessing}
            >
              📷 Use Camera
            </button>
            
            {error && <div className="error-message">{error}</div>}
            {isProcessing && (
              <div className="processing">
                <div className="spinner"></div>
                <p>Analyzing image...</p>
              </div>
            )}
          </div>
        ) : (
          <div className="camera-active">
            <video 
              ref={videoRef} 
              autoPlay 
              playsInline
              className="video-feed"
            />
            <canvas ref={canvasRef} style={{ display: 'none' }} />
            
            <div className="camera-overlay">
              <div className="camera-frame"></div>
              <p className="instruction">Position landmark in frame</p>
            </div>
          </div>
        )}
      </div>

      <div className="camera-controls">
        {mode === 'camera' ? (
          <>
            <button
              className="capture-button"
              onClick={capturePhoto}
              disabled={isProcessing}
            >
              {isProcessing ? '🔍 Analyzing...' : '📸 Capture'}
            </button>
            <button
              className="back-button"
              onClick={stopCamera}
            >
              ← Back to Upload
            </button>
          </>
        ) : (
          <button
            className="back-button"
            onClick={() => navigateTo('home')}
          >
            ← Back to Home
          </button>
        )}
      </div>
    </div>
  );
}

export default Camera;
