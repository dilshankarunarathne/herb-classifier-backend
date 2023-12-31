import mysql.connector
from mysql.connector import errorcode

"""
    middleware for accessing the herb database and performing CRUD operations on the herbs table
"""


class HerbDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        if self.cnx is not None:
            self.cnx.close()

    def get_disease(self, herb):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT disease FROM herbs WHERE herb = %s"
            cursor.execute(query, (herb, ))
            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return None
            return rows
        except mysql.connector.Error as err:
            print(err)

    def get_herb(self, disease):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT herb FROM herbs WHERE disease = %s"
            cursor.execute(query, (disease, ))
            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return None
            return rows
        except mysql.connector.Error as err:
            print(err)
