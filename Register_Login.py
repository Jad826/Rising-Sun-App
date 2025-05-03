import locate_client
import mysql.connector

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
  contactnum = int(input("put you contactnumber: ")
  cursor.execute("INSERT INTO account (username, password, contact_num) VALUES (%s, %s, %s)"(name, password, contact_num))
  db.commit()
                   
def login():
    name = input("put your name: ")
    password = input("put your password: ")
    cursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (name, password))
    db.commit()
              









