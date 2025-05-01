import requests
from geopy.geocoders import Nominatim

ip_data = requests.get("https://ipinfo.io/json").json()
location = ip_data['loc']
latitude, longitude = map(float, location.split(','))

geolocator = Nominatim(user_agent="geoapi")
address = geolocator.reverse((latitude, longitude))


input("Welcome To The Testing Python Client For The Geolocation API\nPress Enter to continue...")
print("Your IP address is: ", ip_data['ip'])
print("Your location is: ", ip_data['loc'])
print(address)