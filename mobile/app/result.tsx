import { useState, useEffect } from 'react';
import { View, Text, ScrollView, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default function Result() {
  const params = useLocalSearchParams();
  const router = useRouter();
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [currentLens, setCurrentLens] = useState(params.lens || 'neutral');

  useEffect(() => {
    fetchInterpretation();
  }, [currentLens]);

  const fetchInterpretation = async () => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}/interpret`, {
        object_id: params.objectId,
        cultural_lens: currentLens,
      });
      setData(response.data);
    } catch (error) {
      console.error('Error fetching interpretation:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#007AFF" />
        <Text style={styles.loadingText}>Loading cultural insights...</Text>
      </View>
    );
  }

  if (!data) {
    return (
      <View style={styles.container}>
        <Text>Error loading data</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>{data.facts.name}</Text>
        <Text style={styles.location}>📍 {data.facts.location}</Text>
      </View>

      {/* Cultural Lens Selector */}
      <View style={styles.lensSelector}>
        <Text style={styles.sectionTitle}>Choose Cultural Lens:</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false}>
          {['neutral', ...data.available_lenses].map((lens: string) => (
            <TouchableOpacity
              key={lens}
              style={[
                styles.lensButton,
                currentLens === lens && styles.lensButtonActive
              ]}
              onPress={() => setCurrentLens(lens)}
            >
              <Text style={[
                styles.lensButtonText,
                currentLens === lens && styles.lensButtonTextActive
              ]}>
                {lens.charAt(0).toUpperCase() + lens.slice(1)}
              </Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>

      {/* Interpretation */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>
          {data.interpretation.perspective}
        </Text>
        <Text style={styles.narrative}>{data.interpretation.narrative}</Text>
        <Text style={styles.emotion}>
          💭 {data.interpretation.emotional_context}
        </Text>
      </View>

      {/* Facts */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Historical Facts</Text>
        <Text style={styles.fact}>📅 Built: {data.facts.built}</Text>
        <Text style={styles.fact}>👤 Builder: {data.facts.builder}</Text>
        <Text style={styles.fact}>🎨 Style: {data.facts.style}</Text>
        <Text style={styles.fact}>🏗️ Material: {data.facts.material}</Text>
      </View>

      {/* Bias Report */}
      <View style={styles.biasSection}>
        <Text style={styles.sectionTitle}>⚖️ Bias Transparency</Text>
        <Text style={styles.biasNote}>{data.bias_report.transparency_note}</Text>
        
        <Text style={styles.subTitle}>Source Distribution:</Text>
        {Object.entries(data.bias_report.source_dominance).map(([source, percent]: [string, any]) => (
          <View key={source} style={styles.sourceBar}>
            <Text style={styles.sourceLabel}>{source.replace('_', ' ')}</Text>
            <View style={styles.barContainer}>
              <View style={[styles.bar, { width: `${percent * 100}%` }]} />
            </View>
            <Text style={styles.sourcePercent}>{Math.round(percent * 100)}%</Text>
          </View>
        ))}

        <Text style={styles.subTitle}>Missing Perspectives:</Text>
        {data.bias_report.missing_perspectives.map((perspective: string, idx: number) => (
          <Text key={idx} style={styles.missingItem}>• {perspective}</Text>
        ))}
      </View>

      <TouchableOpacity
        style={styles.backButton}
        onPress={() => router.push('/')}
      >
        <Text style={styles.backButtonText}>← Back to Home</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 10,
    color: '#666',
  },
  header: {
    backgroundColor: 'white',
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  location: {
    fontSize: 16,
    color: '#666',
  },
  lensSelector: {
    backgroundColor: 'white',
    padding: 15,
    marginTop: 10,
  },
  lensButton: {
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 20,
    backgroundColor: '#f0f0f0',
    marginRight: 10,
  },
  lensButtonActive: {
    backgroundColor: '#007AFF',
  },
  lensButtonText: {
    color: '#333',
    fontWeight: '600',
  },
  lensButtonTextActive: {
    color: 'white',
  },
  section: {
    backgroundColor: 'white',
    padding: 20,
    marginTop: 10,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  narrative: {
    fontSize: 16,
    lineHeight: 24,
    color: '#333',
    marginBottom: 10,
  },
  emotion: {
    fontSize: 14,
    color: '#666',
    fontStyle: 'italic',
  },
  fact: {
    fontSize: 15,
    marginVertical: 5,
    color: '#333',
  },
  biasSection: {
    backgroundColor: '#fff9e6',
    padding: 20,
    marginTop: 10,
  },
  biasNote: {
    fontSize: 14,
    color: '#666',
    marginBottom: 15,
    fontStyle: 'italic',
  },
  subTitle: {
    fontSize: 16,
    fontWeight: '600',
    marginTop: 15,
    marginBottom: 10,
  },
  sourceBar: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 5,
  },
  sourceLabel: {
    width: 120,
    fontSize: 12,
  },
  barContainer: {
    flex: 1,
    height: 20,
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
    overflow: 'hidden',
    marginHorizontal: 10,
  },
  bar: {
    height: '100%',
    backgroundColor: '#FF9500',
  },
  sourcePercent: {
    width: 40,
    fontSize: 12,
    textAlign: 'right',
  },
  missingItem: {
    fontSize: 14,
    color: '#666',
    marginVertical: 3,
  },
  backButton: {
    backgroundColor: '#007AFF',
    padding: 15,
    margin: 20,
    borderRadius: 10,
    alignItems: 'center',
  },
  backButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
});
