#Imports
import mysql.connector
import time
import requests
from geopy.geocoders import Nominatim

db = mysql.connector.connect(
  host = "localhost",
    user="root",
    password="",
    database="risingsun_db"
)

cursor = db.cursor()

#Request user location 
ip_data = requests.get("https://ipinfo.io/json").json()
location = ip_data['loc']
latitude, longitude = map(float, location.split(','))

#Get address based on lat(latitude) and lon(longitude)
geolocator = Nominatim(user_agent="geoapi")
address = geolocator.reverse((latitude, longitude))

def SeeLocation():
  print("Your IP address is: ", ip_data['ip'])
  print("Your location is: ", ip_data['loc'])
  print(address)
  time.sleep(2)
  geolocator()

def OtherUsersReg():
  menu = input("do you want to see others pepole region: ")
  if menu == "yes":
    cursor.execute("SELECT ALL username, region FROM `account`")
    accounts = cursor.fetchall()
    for username, region in accounts:
      print(f"Username: {username}, Region: {region}")
      time.sleep(2)
      geolocator()
  elif menu == "no":
    geolocator()    

def OtherUsersloc():
    menu = input("do you want to see others pepole location: ")
    if menu == "yes":
        cursor.execute("SELECT username, region FROM `account`")  # Use region, not location
        accounts = cursor.fetchall()
        for username, region in accounts:
            print(f"Username: {username}, Region: {region}")
            time.sleep(2)
        geolocator()  # Move this outside the for loop
    elif menu == "no":
        geolocator()
      
#User Interface
def geolocator():
  menu = int(input("\n\nWelcome To The Testing Python Client For RisingSun! Choose The 3 Options\n 1.See Your Location \n 2.See Other Users \n 3.See Weather In Other Location \n 4.Exit \n What Do You Choose: "))
  if menu == 1:
    SeeLocation()
  elif menu == 2:
    OtherUsersloc()  
  elif menu == 3:
    OtherUsersReg()  
 
