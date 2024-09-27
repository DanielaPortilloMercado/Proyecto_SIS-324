# product_service.py
from controllers.product_controller import ProductController

class ProductService:
    def __init__(self):
        self.product_controller = ProductController()

    def add_product(self, name, price, category_id):
        return self.product_controller.add_product(name, price, category_id)

    def update_product(self, product_id, name, price, category_id):
        return self.product_controller.update_product(product_id, name, price, category_id)

    def delete_product(self, product_id):
        return self.product_controller.delete_product(product_id)

    def get_all_products(self):
        return self.product_controller.get_all_products()

    def get_product_by_id(self, product_id):
        return self.product_controller.get_product_by_id(product_id)

    def search_products(self, query):
        return self.product_controller.search_products(query)
