"""
Get accurate coordinates for landmarks using PositionStack API
"""
import requests
import json

API_KEY = "1404c282815f566233229360f79e9f50"
BASE_URL = "http://api.positionstack.com/v1/forward"

landmarks = [
    {"id": "taj_mahal", "name": "Taj Mahal", "query": "Taj Mahal, Agra, India"},
    {"id": "eiffel_tower", "name": "Eiffel Tower", "query": "Eiffel Tower, Paris, France"},
    {"id": "statue_liberty", "name": "Statue of Liberty", "query": "Statue of Liberty, New York, USA"},
    {"id": "colosseum", "name": "Colosseum", "query": "Colosseum, Rome, Italy"},
    {"id": "great_wall", "name": "Great Wall", "query": "Great Wall of China, Beijing, China"},
    {"id": "pyramids_giza", "name": "Pyramids of Giza", "query": "Pyramids of Giza, Cairo, Egypt"},
    {"id": "machu_picchu", "name": "Machu Picchu", "query": "Machu Picchu, Peru"},
    {"id": "christ_redeemer", "name": "Christ the Redeemer", "query": "Christ the Redeemer, Rio de Janeiro, Brazil"},
    {"id": "big_ben", "name": "Big Ben", "query": "Big Ben, London, UK"},
    {"id": "stonehenge", "name": "Stonehenge", "query": "Stonehenge, Wiltshire, UK"},
    {"id": "acropolis", "name": "Acropolis", "query": "Acropolis, Athens, Greece"},
    {"id": "petra", "name": "Petra", "query": "Petra, Jordan"},
    {"id": "angkor_wat", "name": "Angkor Wat", "query": "Angkor Wat, Cambodia"}
]

def get_coordinates(query):
    """Get coordinates for a location"""
    try:
        params = {
            'access_key': API_KEY,
            'query': query,
            'limit': 1
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if data.get('data') and len(data['data']) > 0:
            result = data['data'][0]
            return {
                'latitude': result['latitude'],
                'longitude': result['longitude'],
                'label': result.get('label', query)
            }
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    print("🗺️  Fetching coordinates for landmarks...")
    print("=" * 60)
    
    results = []
    
    for landmark in landmarks:
        print(f"\n📍 {landmark['name']}...")
        coords = get_coordinates(landmark['query'])
        
        if coords:
            landmark_data = {
                'id': landmark['id'],
                'name': landmark['name'],
                'country': landmark['query'].split(',')[-1].strip(),
                'latitude': coords['latitude'],
                'longitude': coords['longitude']
            }
            results.append(landmark_data)
            print(f"   ✅ Lat: {coords['latitude']}, Lon: {coords['longitude']}")
        else:
            print(f"   ❌ Failed to get coordinates")
    
    # Save to file
    with open('landmark_coordinates.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "=" * 60)
    print(f"✅ Saved {len(results)} landmarks to landmark_coordinates.json")
    print("\nYou can now use these coordinates in your map!")

if __name__ == "__main__":
    main()
