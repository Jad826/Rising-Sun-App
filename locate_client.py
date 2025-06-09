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
  otherusersregion = input("what user do you want to search and i will serach the region")
  cursor.execute("SELECT region FROM accounr WHERE username = %s", (otherusersregion,))
  result = cursor.fetchone()
  if result:
    print(f"Region For {otherusersregion}: {result[0]}")
    geolocator()
  else:
    print(f"no region found for user {otherusersregion}")
    geolocator()
def OtherUsersloc():
  #the input of the function
  usersearchloc = input("what user do you want to search and i will search the location: ")
  #will execute an sql query that will see the database and selcet the user
  cursor.execute("SELECT location FROM account WHERE username = %s", (usersearchloc,))
  #the fetchone will return the single string
  result = cursor.fetchone()
  #it will check if the username is in the database or is not it will recive an error
  #and the result 0 will return a single inetger so it only seraches up the users location that you want to see
  if result:
    print(f"Location for {usersearchloc}: {result[0]}")
    geolocator()
  else:
    print(f"No location found for user {usersearchloc}")
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
 
