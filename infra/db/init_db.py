import sqlite3
from pathlib import Path

def init_db():
    schema_path = Path(__file__).parent / "schema.sql"

    connection = sqlite3.connect('database.db')

    with open(schema_path, "r") as f:
        connection.executescript(f.read())

    cur = connection.cursor()
    cur.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", 
                ("1984", "George Orwell", 1))
    cur.execute("INSERT INTO users (name) VALUES (?)", 
                ("Alice",))
    cur.execute("INSERT INTO loans (book_id, user_id) VALUES (?, ?)", 
                (1, 1))
    connection.commit()
    connection.close()
                                                            

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
