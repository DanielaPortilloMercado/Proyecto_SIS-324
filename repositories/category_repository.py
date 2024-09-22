import sqlite3
from models.category import Category

class CategoryRepository:
    def __init__(self):
        self.db_file = 'users.db'

    def get_all_categories(self):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categories")
        rows = cursor.fetchall()
        connection.close()
        return [Category(category_id=row[0], name=row[1]) for row in rows]
