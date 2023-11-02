import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self, host: str, user: str, password: str, database: str):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                passwd=password,
                database=database
            )
            if self.connection.is_connected():
                print("MySQL Database connection successful")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection = None

    def get_connection(self):
        return self.connection
    
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL Database connection closed")

