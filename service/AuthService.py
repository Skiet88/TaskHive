from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from models.User import User
from sqlite3 import connect

# The file path to the SQLite database ("TaskHive.db")
DB = Config.DB_PATH


class AuthService:
    """
      Handles everything related to logging users in and changing their passwords.
    """

    def authenticate_user(self, email, password):
        """
           Check if the given email/password combination is valid.
           Returns a User object if successful, or None if not.
        """
        # Opens a connection to the database which will automatically closed at the end of this block
        with connect(DB) as conn:
            # Fetch the user by email
            row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
            if not row:
                return None

            # Create a User object from the row data
            user = User(*row)

            # Check if the provided password matches the stored hash
            if check_password_hash(user.password_hash, password):
                return user
            return None

    # Change the user's password to a new one.
    def change_password(self, user_id, new_password):
        """
           Change the password for the user with the given user_id.
           The new password is hashed before storing it in the database.
        """
        hashed = generate_password_hash(new_password)
        with connect(DB) as conn:
            conn.execute("UPDATE users SET hash = ? WHERE id = ?", (hashed, user_id))
            conn.commit()