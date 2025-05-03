import mysql.connector

# Connect the db
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="risingsun_db"
)

#Check connection
if db.is_connected():
    print("Connected to MySQL database")

# Close connection
db.close()

