# category_repository.py
import sqlite3
from models.category import Category

class CategoryRepository:
    def __init__(self):
        self.db_file = 'users.db'

    def create_table(self):
        """Crea la tabla de categorías si no existe."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                );
            """)
            connection.commit()
    
    def initialize_categories(self):
        """Inserta categorías predeterminadas si la tabla está vacía."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM categories")
            count = cursor.fetchone()[0]
            if count == 0:
                categories = ['Hombres', 'Mujeres', 'Niños']
                cursor.executemany("INSERT INTO categories (name) VALUES (?)", [(name,) for name in categories])
                connection.commit()

    def get_all_categories(self):
        """Obtiene todas las categorías."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM categories")
            rows = cursor.fetchall()
        
        return [Category(category_id=row[0], name=row[1]) for row in rows]
