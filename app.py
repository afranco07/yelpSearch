from flask import Flask, jsonify, request
from config_keys import YELP_API_KEY
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/yelp', methods=['POST'])
def get_restaurants():
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    radius = request.json['radius']
    URL = f'https://api.yelp.com/v3/businesses/search?latitude={latitude}&longitude={longitude}&radius={radius}'
    HEADERS = {
        'Authorization': f'Bearer {YELP_API_KEY}',
        'Access-Control-Allow-Origin': '*'
    }
    r = requests.get(url=URL, headers=HEADERS)
    data = r.json()
    return jsonify(data)