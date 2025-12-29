# src/database.py

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    """
    Create a MySQL database connection
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Example usage
if __name__ == "__main__":
    connection = create_connection(
        "localhost",  # host
        "root",       # username
        "password",   # password
        "real_estate" # database name
    )
