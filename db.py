#The os module in Python provides a way to interact with the operating system.
import os
#The psycopg2 module provides a pool submodule that allows you to create and manage a connection pool for PostgreSQL database.
from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
    1, 80,
    database=os.getenv('DB_NAME'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_POST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS')
)

# initializes the connection pool and defines a db class with an __init__ method and a select method.
class db:
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool
# a connection is obtained from the connection pool using self.pool.getconn(),
# a cursor is created on the obtained connection using conn.cursor().
    def select(self):
        conn = self.pool.getconn()
        cursor = conn.cursor()
#The SELECT query is executed using cursor.execute()
        cursor.execute(f"SELECT*FROM {self.table}")

#The rows returned by the query are fetched using cursor.fetchall() and stored in the rows variable.
        rows = cursor.fetchall()

        return rows



