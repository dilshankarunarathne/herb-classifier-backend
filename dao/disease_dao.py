import mysql.connector
from mysql.connector import errorcode

"""
    middleware for accessing the herb database and performing CRUD operations on the disease table
"""

class DiseaseDAO:
    def __int__(self):
