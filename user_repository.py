import sqlite3
from user import User

class UserRepository:
    def __init__(self):
        self.db_file = 'users.db'

    def get_all_users(self):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        connection.close()
        return [User(user_id=row[0], username=row[1], password=row[2]) for row in rows]

    def get_user_by_username(self, username):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return User(user_id=row[0], username=row[1], password=row[2])
        return None

    def add_user(self, user):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
        connection.commit()
        connection.close()
