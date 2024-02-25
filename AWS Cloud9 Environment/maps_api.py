# maps_api.py

import requests
from config import API_KEY

def get_directions(origin, destination):
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'origin': origin,
        'destination': destination,
        'key': API_KEY,
    }
    response = requests.get(endpoint, params=params)
    directions = response.json()

    if directions.get("status") == "OK":
        steps = directions['routes'][0]['legs'][0]['steps']
        directions_info = [{
            'instruction': step['html_instructions'], 
            'distance': step['distance']['text']
        } for step in steps]
        return directions_info
    else:
        return None