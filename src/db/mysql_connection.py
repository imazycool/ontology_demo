import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from common.exceptions import  DatabaseAlreadyConnectedError, DatabaseNotConnectedError


class MySQLConnection:

    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.connection = None
        
        

    def connect(self):
        """
        Establish a connection to the MySQL database.
        Returns:
            MySQLConnection: Active MySQL connection object.
        Raises:
            Exception: If the database connection fails.
        """
        if self.connection:
            raise DatabaseAlreadyConnectedError(
                "Database is already connected."
            )
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if self.connection.is_connected():
                # print("Successfully connected to MySQL database")
                return self.connection
        except Exception:
            raise
        
        

    def disconnect(self):
        """
        Close the active database connection.
        """
        if self.connection.is_connected():
            self.connection.close() 
        self.connection = None



    def execute_query(self, query, params=None):
        if not (self.connection.is_connected()):
            raise DatabaseNotConnectedError(
                "Database not connected."
            )
        try:
            if self.connection.is_connected():
                cursor=self.connection.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                rows=cursor.fetchall()
                return rows 
        except Exception:
            raise 
        finally:
            if self.connection.is_connected() and 'cursor' in locals():
                cursor.close()
                
    
    def execute_single(self, query, params=None):
        if not (self.connection.is_connected()):
            raise DatabaseNotConnectedError(
                "Database not connected."
            )
        try:
            if self.connection.is_connected():
                cursor=self.connection.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                first_row=cursor.fetchone()
                return first_row 
        except Exception:
            raise 
        finally:
            if self.connection.is_connected() and 'cursor' in locals():
                cursor.close()
                