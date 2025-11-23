import sqlite3
import os

DB_PATH = "database.db"  

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
