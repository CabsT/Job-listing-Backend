#The os module in Python provides a way to interact with the operating system.
import os
#The psycopg2 module provides a pool submodule that allows you to create and manage a connection pool for PostgreSQL database.
from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
    1, 80,
    database=os.getenv('DB_NAME'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS')
)

class db:
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool

    def select(self):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        query = f"SELECT * FROM {self.table}"
        cursor.execute(query)
        job_data = cursor.fetchall()

        self.pool.putconn(conn)

        return job_data
    
    def insert(self, data):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        keys = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table} ({keys}) VALUES ({placeholders})"
        cursor.execute(query, tuple(data.values()))
        conn.commit()

      
  