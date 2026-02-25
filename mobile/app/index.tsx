import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';

export default function Home() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🌍 CultureLens</Text>
      <Text style={styles.subtitle}>
        Discover art and heritage through multiple cultural perspectives
      </Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push('/camera')}
      >
        <Text style={styles.buttonText}>📷 Scan Monument</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={[styles.button, styles.secondaryButton]}
        onPress={() => router.push({ pathname: '/result', params: { objectId: 'taj_mahal', lens: 'local' } })}
      >
        <Text style={styles.buttonText}>🧪 Demo: Taj Mahal</Text>
      </TouchableOpacity>

      <View style={styles.features}>
        <Text style={styles.featureText}>✓ Edge AI (Privacy-First)</Text>
        <Text style={styles.featureText}>✓ Multiple Cultural Lenses</Text>
        <Text style={styles.featureText}>✓ Bias Transparency</Text>
        <Text style={styles.featureText}>✓ Community Perspectives</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 48,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    textAlign: 'center',
    color: '#666',
    marginBottom: 40,
    paddingHorizontal: 20,
  },
  button: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 40,
    paddingVertical: 15,
    borderRadius: 10,
    marginVertical: 10,
    minWidth: 250,
  },
  secondaryButton: {
    backgroundColor: '#34C759',
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: '600',
    textAlign: 'center',
  },
  features: {
    marginTop: 40,
    alignItems: 'flex-start',
  },
  featureText: {
    fontSize: 14,
    color: '#666',
    marginVertical: 5,
  },
});
