from flask import Blueprint, render_template, request, jsonify
from app.services.solver import calculate_trajectory
from app.services.weather import get_weather_data

ballistics_bp = Blueprint('ballistics', __name__)

@ballistics_bp.route('/calculate', methods=['POST'])
def calculate():
    initial_velocity = float(request.form['initial_velocity'])
    angle = float(request.form['angle'])
    use_weather = request.form.get('use_weather')
    latitude = float(request.form.get('latitude', 0))
    spin_rate = float(request.form.get('spin_rate', 0))

    weather_data = None
    if use_weather:
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        weather_data = get_weather_data(lat, lon)

    trajectory = calculate_trajectory(initial_velocity, angle, weather_data, latitude, spin_rate)
    return render_template('results.html', trajectory=trajectory)

@ballistics_bp.route('/get_location', methods=['POST'])
def get_location():
    # In a real app, you would get the user's location from the browser
    # using the Geolocation API. For now, we'll just use a dummy location.
    return jsonify({'lat': 37.7749, 'lon': -122.4194})