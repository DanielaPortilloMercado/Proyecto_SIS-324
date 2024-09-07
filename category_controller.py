from category import Category

class CategoryController:
    def __init__(self):
        # Esto puede conectarse a una base de datos si es necesario.
        self.categories = [
            Category(category_id=1, name="Hombres"),
            Category(category_id=2, name="Mujeres"),
            Category(category_id=3, name="Niños")
        ]

    def get_all_categories(self):
        return self.categories
