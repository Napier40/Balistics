import os
import requests

def get_weather_data(lat, lon):
    """
    Gets the weather data for a given latitude and longitude.

    Args:
        lat: The latitude.
        lon: The longitude.

    Returns:
        A dictionary containing the weather data.
    """
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    return response.json()
