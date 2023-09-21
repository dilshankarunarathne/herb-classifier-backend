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

    def get_disease_details(self, disease):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT * FROM disease WHERE disease = %s"
            values = disease
            cursor.execute(query, values)
            self.cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(err)
