import sqlite3

def init_db():

    # Initialize the SQLite database
    connection = sqlite3.connect("TaskHive.db")
    cursor = connection.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        hash TEXT NOT NULL
    )
    """)

    # Create tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        created_at TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    connection.commit()
    connection.close()
    #print("Database initialized!")

if __name__ == "__main__":
    init_db()
