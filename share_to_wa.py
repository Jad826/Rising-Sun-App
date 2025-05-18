import pywhatkit
from datetime import datetime
import requests

# Request user location
ip_data = requests.get("https://ipinfo.io/json").json()
location = ip_data['loc']
latitude, longitude = map(float, location.split(','))

# API key
api_key = "6beab64899071c31f2ddb0d7ef384a5c"  # Replace with your actual API key

# Base URL
user_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

# Make API request
response = requests.get(user_url)

# Show the result
if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    all_weather_data = f"\nWeather in {city_name}\nTemperature: {temp}°C\nCondition: {description}"
else:
    print("Failed to retrieve data to send:", response.json().get("message"))
# Note: Make sure to replace "your_api_key" with your actual OpenWeatherMap API key.

now = datetime.now()
hour = now.hour
minute = now.minute + 2

phone_number=input("Welcome, to who do you want to send the weather of your region to?(enter their phone number): ")

pywhatkit.sendwhatmsg_instantly(phone_number, all_weather_data, wait_time=10, tab_close=True)
