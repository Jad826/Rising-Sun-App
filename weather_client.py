import requests

# Request user location
ip_data = requests.get("https://ipinfo.io/json").json()
location = ip_data['loc']
latitude, longitude = map(float, location.split(','))

# API key
api_key = ""  # Replace with your actual API key

# Cities
city1 = "Saida"
city2 = "Beirut"
city3 = "Nabatîyé et Tahta"

# Base URLs
user_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
saida_url = f"https://api.openweathermap.org/data/2.5/weather?q={city1}&appid={api_key}&units=metric"
beirut_url = f"https://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}&units=metric"
nabatieh_url = f"https://api.openweathermap.org/data/2.5/weather?q={city3}&appid={api_key}&units=metric"

# User Interface
ui = int(input("\nWelcome to the Geolocation Weather Client\n"
               " · Enter 1 for your region's weather\n"
               " · Enter 2 for Saida\n"
               " · Enter 3 for Beirut\n"
               " · Enter 4 for Nabatieh\n"
               " · Enter 5 to exit\n"))

if ui == 1:
    selected_url = user_url
elif ui == 2:
    selected_url = saida_url
elif ui == 3:
    selected_url = beirut_url
elif ui == 4:
    selected_url = nabatieh_url
elif ui == 5:
    print("Exiting...")
    exit()
else:
    print("Invalid input. Please enter a number between 1 and 5.")
    exit()

# Make API request
response = requests.get(selected_url)

# Show the result
if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    
    print(f"\nWeather in {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description}")
else:
    print("Failed to retrieve data:", response.json().get("message"))
# Note: Make sure to replace "your_api_key" with your actual OpenWeatherMap API key.
