import requests
from geopy.geocoders import Nominatim

#Request user location 
ip_data = requests.get("https://ipinfo.io/json").json()
location = ip_data['loc']
latitude, longitude = map(float, location.split(','))

# API key
api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key(get on https://openweathermap.org/api) just make an account and verify through email and get the key

#Cities
city1 = "Saida"
city2 = "Beirut"
city3 = "Nabatieh"

#Base URL
url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

#Request
response = requests.get(url)

#Show the error if not working and if working show the data
if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    
    print(f"Weather in {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description}")
else:
    print("Failed to retrieve data:", response.json().get("message"))
