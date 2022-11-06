import os

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection


class Datastore:
    connection: MySQLConnection | None = None
    db_name = os.getenv('db_name')
    db_user = os.getenv('db_user')
    db_pass = os.getenv('db_pass')
    db_host = os.getenv('db_host')

    def __init__(self):
        self.db_name = os.getenv('db_name')
        self.db_user = os.getenv('db_user')
        self.db_pass = os.getenv('db_pass')
        self.db_host = os.getenv('db_host')
        self.establish_connection()

    @classmethod
    def establish_connection(cls):
        try:
            cls.connection = mysql.connector.connect(
                host=cls.db_host,
                user=cls.db_user,
                passwd=cls.db_pass,
                database=cls.db_name
            )

            if cls.connection.is_connected():
                print("Connected to database: ", cls.connection.cursor().fetchone())
        except Error as err:
            print(f'Error while connecting to sql database: {err}')

    @classmethod
    def fetch_connection(cls) -> MySQLConnection | None:
        # check if connection exists. If it does, return said connection. Else Try connecting then returning.
        # Else. Return none
        if cls.connection is not None:
            return cls.connection

        cls.establish_connection()
        if cls.connection is not None:
            return cls.connection

        return None
