import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection


class Datastore:
    def __init__(self, db_user, db_pass, db_name, db_host):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.connection: MySQLConnection | None = None

    def establish_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                passwd=self.db_pass,
                database=self.db_name
            )

            if self.connection.is_connected():
                print("Connected to database: ", self.connection.cursor().fetchone())
        except Error as err:
            print(f'Error while connecting to sql database: {err}')

    def fetch_connection(self) -> MySQLConnection | None:
        # check if connection exists. If it does, return said connection. Else Try connecting then returning.
        # Else. Return none
        if self.connection.is_connected():
            return self.connection

        self.establish_connection()
        if self.connection.is_connected():
            return self.connection

        return None
