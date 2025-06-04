from flask_login import UserMixin

# This file defines the User model for the application.
class User(UserMixin):
    def __init__(self, id=None, name=None, surname=None, email=None, password_hash=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password_hash = password_hash

    def __str__(self):
        return f"User: {self.id} {self.name} {self.surname} ({self.email})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "password_hash": self.password_hash
        }
