from config import Config
from models.User  import User
from werkzeug.security import generate_password_hash, check_password_hash
from sqlite3 import connect

# The file path to the SQLite database ("TaskHive.db")
DB = Config.DB_PATH

class UserService:
    """
    Handles everything related to users, such as creating, retrieving, updating, and deleting users.
    """
    def create_user(self, name, surname, email, password):

        #Hash the password before storing it using Werkzeug's security module
        password_hash = generate_password_hash(password)
        with connect(DB) as conn:
            conn.execute("""
                INSERT INTO users (name, surname, email, hash)
                VALUES (?, ?, ?, ?)
            """, (name, surname, email, password_hash))
            conn.commit()

    def get_by_id(self, user_id):
        with connect(DB) as conn:
            row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            return User(*row) if row else None

    def get_by_email(self, email):
        with connect(DB) as conn:
            row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
            return User(*row) if row else None

    def update_user(self, user_id, name, surname, email):
        with connect(DB) as conn:
            conn.execute("""
                UPDATE users
                SET name = ?, surname = ?, email = ?
                WHERE id = ?
            """, (name, surname, email, user_id))
            conn.commit()

    def delete_user(self, user_id):
        with connect(DB) as conn:
            conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()

