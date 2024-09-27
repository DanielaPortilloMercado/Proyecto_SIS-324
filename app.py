from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, abort
from controllers.user_controller import UserController
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from repositories.product_repository import ProductRepository  # Asegúrate de importar esto
from repositories.category_repository import CategoryRepository  # Asegúrate de importar esto

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Inicializar controladores
user_controller = UserController()
category_controller = CategoryController()
product_controller = ProductController()

# Inicializar repositorios
product_repo = ProductRepository()
category_repo = CategoryRepository()

# Crear las tablas si no existen
product_repo.create_table()
category_repo.create_table()

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Registro de usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_controller.register_user(username, password)
        flash(f"User {username} registered successfully.")
        return redirect(url_for('login'))
    return render_template('register.html')

# Login de usuarios
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_controller.login_user(username, password):
            flash("Login successful!")
            return redirect(url_for('categories'))
        else:
            flash("Invalid credentials, try again.")
    return render_template('login.html')

# Listado de categorías
@app.route('/categories')
def categories():
    categories = category_controller.get_all_categories()
    return render_template('categories.html', categories=categories)

# Filtrar productos por categoría
@app.route('/categories/<int:category_id>/products', methods=['GET'])
def products_by_category(category_id):
    products = category_controller.get_products_by_category(category_id)
    return render_template('products.html', products=products)

# Listar productos
@app.route('/products', methods=['GET'])
def list_products():
    products = product_controller.get_all_products()
    return render_template('products.html', products=products)

# Buscar productos
@app.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    products = product_controller.search_products(query)
    return render_template('products.html', products=products)

# Añadir un producto
@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category_id = request.form['category_id']
        product_controller.add_product(name, price, category_id)
        flash(f"Product {name} added successfully.")
        return redirect(url_for('list_products'))
    categories = category_controller.get_all_categories()
    return render_template('add_product.html', categories=categories)

# Editar un producto
@app.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    product = product_controller.get_product_by_id(product_id)
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category_id = request.form['category_id']
        product_controller.update_product(product_id, name, price, category_id)
        flash(f"Product {name} updated successfully.")
        return redirect(url_for('list_products'))
    categories = category_controller.get_all_categories()
    return render_template('edit_product.html', product=product, categories=categories)

# Eliminar un producto
@app.route('/products/<int:product_id>/delete', methods=['POST'])
def delete_product(product_id):
    product_controller.delete_product(product_id)
    flash("Product deleted successfully.")
    return redirect(url_for('list_products'))

# API: Obtener todos los productos
@app.route('/api/products', methods=['GET'])
def api_get_products():
    products = product_controller.get_all_products()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'category_id': product.category_id
    } for product in products])

# API: Añadir un producto
@app.route('/api/products', methods=['POST'])
def api_add_product():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    category_id = data.get('category_id')

    # Verificar campos obligatorios
    if not name or not price or not category_id:
        abort(400, description="Name, price, and category_id are required.")

    product_controller.add_product(name, price, category_id)
    return jsonify({"message": "Product added successfully."}), 201

if __name__ == '__main__':
    app.run(debug=True)
