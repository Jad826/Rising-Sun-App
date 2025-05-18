import requests
from geopy.geocoders import Nominatim

#Request user location 
ip_data = requests.get("https://ipinfo.io/json").json()
location = ip_data['loc']
latitude, longitude = map(float, location.split(','))

# API key
api_key = "your api key"  # Replace with your OpenWeatherMap API key(get on https://openweathermap.org/api) just make an account and verify through email and get the key

#Cities
city1 = "Saida"
city2 = "Beirut"
city3 = "Nabatieh"

#Base URLs
user_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
saida_url = f"https://api.openweathermap.org/data/2.5/weather?q={city1}&appid={api_key}&units=metric"
beirut_url = f"https://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}&units=metric"
nabatieh_url = f"https://api.openweathermap.org/data/2.5/weather?q={city3}&appid={api_key}&units=metric"

#User Interface
ui=int(input("\n\nWelcome To The Testing Python Client For The Geolocation API\n · Enter 1 to see your region's weather\n · Enter 2 to see the weather of Saida\n · Enter 3 to see the weather of Beirut\n · Enter 4 to see the weather of Nabatieh\n · Enter 5 to exit\n"))
if ui == 1:
    response = user_url
elif ui == 2:
    response = saida_url
elif ui == 3:
    response = beirut_url
elif ui == 4:
    response = nabatieh_url
elif ui == 5:
    print("Exiting...")
    exit()
else:
    print("Invalid input. Please enter a number between 1 and 5.")
    ui=int(input("\n\nWelcome To The Testing Python Client For The Geolocation API\n · Enter 1 to see your region's weather\n · Enter 2 to see the weather of Saida\n · Enter 3 to see the weather of Beirut\n · Enter 4 to see the weather of Nabatieh\n · Enter 5 to exit\n"))

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
