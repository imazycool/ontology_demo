import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from common.exceptions import  DatabaseAlreadyConnectedError


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
        if self.connection:
            self.connection.close() 
        self.connection = None



    def execute_query(self, query):
        pass