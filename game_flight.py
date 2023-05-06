import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight',
            user='root',
            password='Ratgai#1!',
            autocommit=True
        )

    def get_conn(self):
        return self.conn