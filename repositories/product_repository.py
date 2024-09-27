import sqlite3
from models.product import Product

class ProductRepository:
    def __init__(self):
        self.db_file = 'users.db'

    def create_table(self):
        """Crea la tabla de productos si no existe."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    category_id INTEGER,
                    FOREIGN KEY (category_id) REFERENCES categories(id)
                );
            """)
            connection.commit()

    def get_all_products(self):
        """Obtiene todos los productos."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
        
        return [Product(product_id=row[0], name=row[1], price=row[2], category_id=row[3]) for row in rows]

    def get_product_by_id(self, product_id):
        """Obtiene un producto por su ID."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
            row = cursor.fetchone()
        
        if row:
            return Product(product_id=row[0], name=row[1], price=row[2], category_id=row[3])
        return None

    def add_product(self, product):
        """Añade un nuevo producto."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                           (product.name, product.price, product.category_id))
            connection.commit()

    def update_product(self, product):
        """Actualiza un producto existente."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE products SET name = ?, price = ?, category_id = ? WHERE id = ?",
                           (product.name, product.price, product.category_id, product.product_id))
            connection.commit()

    def delete_product(self, product_id):
        """Elimina un producto por su ID."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            connection.commit()

    def search_products(self, query):
        """Busca productos por nombre."""
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products WHERE name LIKE ? OR category_id LIKE ? OR price LIKE ?",
                           (f'%{query}%', f'%{query}%', f'%{query}%'))
            rows = cursor.fetchall()
        
        return [Product(product_id=row[0], name=row[1], price=row[2], category_id=row[3]) for row in rows]
