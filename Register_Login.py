import locate_client
import mysql.connector
import menu_handler

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="",
    database="risingsun_db"
)

cursor = db.cursor()



def register():
    name = input("put your name: ")
    password = input("put your password: ")
    contactnum = input("put you contactnumber: ")
    cursor.execute("INSERT INTO account (username, password, contact_num) VALUES (%s, %s, %s)", (name, password, contactnum))
    db.commit()
    locate_client.geolocator()                 
                   
def login():
    name = input("put your name: ")
    password = input("put your password: ")
    cursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (name, password))
    result = cursor.fetchall()
    if result:
        print("Login successful!")
        locate_client.geolocator() 
    else:
        print("Invalid username or password.")
        menu_handler.menu()   
              
              



