from repositories.product_repository import ProductRepository
from models.product import Product

class ProductController:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all_products(self):
        products = self.product_repository.get_all_products()
        print(products)  # Para verificar el contenido
        return products  # Asegúrate de que aquí devuelves objetos Product

    def get_product_by_id(self, product_id):
        return self.product_repository.get_product_by_id(product_id)

    def add_product(self, name, price, category_id):
        product = Product(product_id=None, name=name, price=price, category_id=category_id)
        self.product_repository.add_product(product)

    def update_product(self, product_id, name, price, category_id):
        product = Product(product_id=product_id, name=name, price=price, category_id=category_id)
        self.product_repository.update_product(product)

    def delete_product(self, product_id):
        self.product_repository.delete_product(product_id)

    def search_products(self, query):
        return self.product_repository.search_products(query)
