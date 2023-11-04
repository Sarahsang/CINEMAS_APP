import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class Database:
    def __init__(self, host: str, user: str, password: str, database: str):
        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5,
                pool_reset_session=True,
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("MySQL Connection pool is created")
        except Error as e:
            print(f"Error: '{e}'")

    def get_connection(self):
        return self.connection_pool.get_connection()

    def close_connection(self, conn):
        if conn:
            conn.close()
