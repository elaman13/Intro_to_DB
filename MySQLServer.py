import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '121212',
        database = 'alx_book_store'
    )

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error while connecting to MYSQL: {e}")
    
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()