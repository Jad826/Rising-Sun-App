import requests

"""Sunrise/Sunset API(API For sunrise and sunset data)"""
def get_sunrise_sunset(lat, lng):
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0"
    response = requests.get(url)
    return response.json()

"""OpenWeatherMap API (API For weather data)"""
def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
