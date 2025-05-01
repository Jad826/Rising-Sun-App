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
            print("MySQL connection is closed")
