from user_repository import UserRepository
from user import User

class UserController:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username, password):
        # Aquí puedes agregar lógica adicional como hashing de contraseñas
        user = User(username=username, password=password)
        self.user_repository.add_user(user)

    def login_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and user.password == password:  # En un entorno real, compara contraseñas hasheadas
            return True
        return False
