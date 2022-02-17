import psycopg2
import os
import logging


class Database:

    def __init__(self):
        self.HOST = os.environ["HOST"]
        self.DATABASE = os.environ["DATABASE"]
        self.USER = os.environ["USER"]
        self.PASSWORD = os.environ["PASSWORD"]
        self.PORT = os.environ["PORT"]

    def connect_db(self):
        conn = psycopg2.connect(
            host=self.HOST,
            database=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD,
            port=self.PORT)

        cur = conn.cursor()
        return cur, conn   