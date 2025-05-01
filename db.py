<<<<<<< HEAD
import mysql.connector

def insert_data(name, email, password):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="risingsun_db"
        )

        cursor = db.cursor()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
=======
import mysql.connector

def insert_data(name, email, password):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="risingsun_db"
        )

        cursor = db.cursor()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
>>>>>>> e2fe9677d9ba4041e20f3b3b2fe8dc23df12bfe1
            print("MySQL connection is closed")