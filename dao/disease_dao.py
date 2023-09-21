import mysql.connector
from mysql.connector import errorcode

"""
    middleware for accessing the herb database and performing CRUD operations on the disease table
"""

class DiseaseDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
