import { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert } from 'react-native';
import { CameraView, useCameraPermissions } from 'expo-camera';
import { useRouter } from 'expo-router';

export default function Camera() {
  const [permission, requestPermission] = useCameraPermissions();
  const [isProcessing, setIsProcessing] = useState(false);
  const router = useRouter();

  if (!permission) {
    return <View />;
  }

  if (!permission.granted) {
    return (
      <View style={styles.container}>
        <Text style={styles.message}>Camera permission required</Text>
        <TouchableOpacity style={styles.button} onPress={requestPermission}>
          <Text style={styles.buttonText}>Grant Permission</Text>
        </TouchableOpacity>
      </View>
    );
  }

  const handleCapture = async () => {
    setIsProcessing(true);
    
    // Simulate edge AI processing
    setTimeout(() => {
      setIsProcessing(false);
      // Mock recognition - in production this would use TensorFlow Lite
      const mockLandmarks = ['taj_mahal', 'colosseum', 'great_wall'];
      const recognized = mockLandmarks[Math.floor(Math.random() * mockLandmarks.length)];
      
      router.push({
        pathname: '/result',
        params: { objectId: recognized, lens: 'neutral' }
      });
    }, 1500);
  };

  return (
    <View style={styles.container}>
      <CameraView style={styles.camera}>
        <View style={styles.overlay}>
          <Text style={styles.instruction}>
            Point camera at a monument or artwork
          </Text>
          <View style={styles.frame} />
        </View>
      </CameraView>

      <View style={styles.controls}>
        <TouchableOpacity
          style={[styles.captureButton, isProcessing && styles.processing]}
          onPress={handleCapture}
          disabled={isProcessing}
        >
          <Text style={styles.captureText}>
            {isProcessing ? '🔍 Analyzing...' : '📸 Capture'}
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
  },
  camera: {
    flex: 1,
  },
  overlay: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  instruction: {
    color: 'white',
    fontSize: 18,
    backgroundColor: 'rgba(0,0,0,0.6)',
    padding: 15,
    borderRadius: 10,
    marginBottom: 20,
  },
  frame: {
    width: 300,
    height: 300,
    borderWidth: 3,
    borderColor: 'white',
    borderRadius: 10,
  },
  controls: {
    position: 'absolute',
    bottom: 40,
    left: 0,
    right: 0,
    alignItems: 'center',
  },
  captureButton: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 50,
    paddingVertical: 20,
    borderRadius: 50,
  },
  processing: {
    backgroundColor: '#666',
  },
  captureText: {
    color: 'white',
    fontSize: 20,
    fontWeight: 'bold',
  },
  message: {
    textAlign: 'center',
    paddingBottom: 10,
    color: 'white',
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 15,
    borderRadius: 10,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
  },
});
