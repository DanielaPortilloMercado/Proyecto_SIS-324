import sqlite3
from models.product import Product

import sqlite3
from models.product import Product

class ProductRepository:
    def __init__(self):
        self.db_file = 'users.db'

    def get_all_products(self):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        connection.close()
        return [Product(product_id=row[0], name=row[1], price=row[2], category_id=row[3]) for row in rows]

    def add_product(self, product):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                       (product.name, product.price, product.category_id))
        connection.commit()
        connection.close()
