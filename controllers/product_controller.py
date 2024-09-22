from repositories.product_repository import ProductRepository
from models.product import Product

class ProductController:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all_products(self):
        return self.product_repository.get_all_products()

    def add_product(self, name, price, category_id):
        product = Product(product_id=None, name=name, price=price, category_id=category_id)
        self.product_repository.add_product(product)
