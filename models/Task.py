from datetime import datetime

# Task model representing a task in the system
class Task:
    def __init__(self, id=None, user_id=None, title=None, description=None, created_at=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return f"Task: {self.title} (Created: {self.created_at})"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }
