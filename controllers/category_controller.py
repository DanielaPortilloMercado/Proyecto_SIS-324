class CategoryController:
    def __init__(self):
        # Categorías definidas estáticamente
        self.categories = [
            {'id': 1, 'name': 'Hombres'},
            {'id': 2, 'name': 'Mujeres'},
            {'id': 3, 'name': 'Niños'}
        ]

     # Productos por categoría
        self.products = {
            1: [{'id': 1, 'name': 'Conjunto deportivo nike', 'price': 111},
                {'id': 2, 'name': 'short', 'price': 50.51}],
            2: [{'id': 3, 'name': 'sudadera', 'price': 15.99},
                {'id': 4, 'name': 'Bandas elasticas', 'price': 5.99}],
            3: [{'id': 5, 'name': 'T-shirt', 'price': 19.99},
                {'id': 6, 'name': 'mochilas', 'price': 49.99}]
        }


    def get_all_categories(self):
        return self.categories
    def get_products_by_category(self, category_id):
        return self.products.get(category_id, [])
