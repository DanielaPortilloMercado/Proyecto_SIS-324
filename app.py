from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, abort
from user_controller import UserController
from category_controller import CategoryController

app = Flask(__name__)
app.secret_key = 'supersecretkey'

user_controller = UserController()
category_controller = CategoryController()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_controller.register_user(username, password)
        flash(f"User {username} registered successfully.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_controller.login_user(username, password):
            flash("Login successful!")
            # Redirigir a la página de categorías después del login exitoso
            return redirect(url_for('categories'))
        else:
            flash("Invalid credentials, try again.")
    return render_template('login.html')

@app.route('/categories')
def categories():
    categories = category_controller.get_all_categories()
    return render_template('categories.html', categories=categories)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = user_controller.user_repository.get_all_users()
    return jsonify([{
        'user_id': user.user_id,
        'username': user.username
    } for user in users])

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    user = user_controller.user_repository.get_user_by_username(username)
    if user:
        return jsonify({
            'user_id': user.user_id,
            'username': user.username
        })
    else:
        abort(404)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        abort(400, description="Username and password are required.")
    
    user_controller.register_user(username, password)
    return jsonify({"message": "User registered successfully."}), 201

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if user_controller.login_user(username, password):
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid credentials."}), 401

if __name__ == '__main__':
    app.run(debug=True)
