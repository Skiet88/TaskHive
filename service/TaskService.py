from config import Config
from models.Task import Task
from sqlite3 import connect
from datetime import datetime

# The file path to the SQLite database ("TaskHive.db")
DB = Config.DB_PATH

class TaskService:
    """
    Handles everything related to tasks, such as creating, retrieving, updating, and deleting tasks.
    """
    def create_task(self, user_id, title, description):
        with connect(DB) as conn:
            conn.execute("""
                INSERT INTO tasks (user_id, title, description, created_at)
                VALUES (?, ?, ?, ?)
            """, (user_id, title, description, datetime.now()))
            conn.commit()

    def get_tasks_for_user(self, user_id):
        with connect(DB) as conn:
            rows = conn.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,)).fetchall()
            return [Task(*row) for row in rows]

    def delete_task(self, task_id, user_id):
        with connect(DB) as conn:
            conn.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
            conn.commit()

    def update_task(self, task_id, user_id, title, description):
        with connect(DB) as conn:
            conn.execute("""
                         UPDATE tasks
                         SET title       = ?,
                             description = ?
                         WHERE id = ?
                           AND user_id = ?
                         """, (title, description, task_id, user_id))
            conn.commit()

    # Retrieves tasks for a user, optionally filtered by title substring and/or date
    def get_tasks_filtered(self, user_id, q=None, date=None):
        """Return tasks filtered by title substring and/or ISO date (YYYY-MM-DD)."""
        sql = "SELECT * FROM tasks WHERE user_id = ?"
        args = [user_id]


        if q:
            sql += " AND title LIKE ?"
            args.append(f"%{q}%")

        if date:
            sql += " AND DATE(created_at) = DATE(?)"
            args.append(date)

        with connect(DB) as conn:
            rows = conn.execute(sql, tuple(args)).fetchall()
            return [Task(*row) for row in rows]
