import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os



class DatabaseAlreadyConnectedError(Exception):
    """
    Raised when attempting to connect while a database
    connection already exists.
    """
    pass



class DatabaseConnectionError(Exception):
    pass





class DatabaseNotConnectedError(Exception):
    pass