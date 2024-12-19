import requests

# Replace with your OpenRouteService API key
API_KEY = '5b3ce3597851110001cf6248cafa909e641941f2af1a76b9c97c0907'
BASE_URL = 'https://api.openrouteservice.org/v2/directions/driving-car'

# Sample coordinates for start and end points (longitude, latitude)
# Coordinates for Patna (Boring Road) and Muzaffarpur (Gobarsahi Road)
start = (85.1467, 25.6077)  # Patna (Longitude, Latitude)
end = (85.3828, 26.1212)    # Muzaffarpur (Longitude, Latitude)

def get_route(start, end):
    headers = {
        'Authorization': API_KEY
    }
    # Define the coordinates for the start and end points in the URL
    params = {
        'start': f'{start[0]},{start[1]}',
        'end': f'{end[0]},{end[1]}'
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    return response.json()

def format_route(route_data):
    # Extract relevant data from the API response
    if 'features' in route_data and len(route_data['features']) > 0:
        route = route_data['features'][0]
        steps = route['properties']['segments'][0]['steps']
        
        for step in steps:
            instruction = step.get('instruction', 'No instruction available')
            distance = step.get('distance', 0) / 1000  # Convert to km
            time = step.get('duration', 0) / 60  # Convert to minutes
            
            print(f"Instruction: {instruction}")
            print(f"Distance: {distance:.1f} km")
            print(f"Time: {int(time)} mins")
            print("-" * 40)

def main():
    route_data = get_route(start, end)
    format_route(route_data)

if __name__ == "__main__":
    main()
