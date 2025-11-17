import sqlite3
import os

DB_PATH = "database.db"  # cria o banco no diretório raiz do projeto

def get_connection():
    return sqlite3.connect(DB_PATH)
