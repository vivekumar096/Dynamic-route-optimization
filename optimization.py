from flask import Flask, request, jsonify
import googlemaps
import os

app = Flask(__name__)

# Initialize Google Maps API client
GMAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your API key
gmaps = googlemaps.Client(key=GMAPS_API_KEY)

@app.route("/")
def home():
    return "Dynamic Route Optimization API is running."

# Route to get optimized directions
@app.route('/optimize_route', methods=['POST'])
def optimize_route():
    try:
        data = request.json
        source = data['source']  # Starting point (latitude, longitude)
        destination = data['destination']  # Destination point (latitude, longitude)

        # Fetch directions with traffic considerations
        directions_result = gmaps.directions(
            source, 
            destination,
            mode="driving",
            departure_time="now",  # Use current time for traffic
            traffic_model="best_guess"
        )

        # Extract relevant route details
        optimized_route = []
        for step in directions_result[0]['legs'][0]['steps']:
            optimized_route.append({
                "instruction": step['html_instructions'],
                "distance": step['distance']['text'],
                "duration": step['duration']['text'],
                "location": step['end_location']
            })

        return jsonify({
            "status": "success",
            "optimized_route": optimized_route
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
