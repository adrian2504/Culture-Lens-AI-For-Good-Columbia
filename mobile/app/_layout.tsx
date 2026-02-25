import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="index" options={{ title: 'CultureLens' }} />
      <Stack.Screen name="camera" options={{ title: 'Scan Monument' }} />
      <Stack.Screen name="result" options={{ title: 'Cultural Insights' }} />
    </Stack>
  );
}
