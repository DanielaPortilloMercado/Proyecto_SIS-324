# category_controller.py
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository

class CategoryController:
    def __init__(self):
        self.category_repository = CategoryRepository()
        self.product_repository = ProductRepository()

    def get_all_categories(self):
        return self.category_repository.get_all_categories()

    def get_products_by_category(self, category_id):
        return self.product_repository.get_products_by_category(category_id)

