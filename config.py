
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "TaskHive.db")


class Config:
    SECRET_KEY = "5z@Y#2G!8$k$M%pN&wXqD^LjA3b*U+vZ"
    DB_PATH = DB_PATH
