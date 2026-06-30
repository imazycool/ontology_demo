import mysql.connector
from dotenv import load_dotenv
import os



class MySQLConnection:

    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.connection = None

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute_query(self, query):
        pass