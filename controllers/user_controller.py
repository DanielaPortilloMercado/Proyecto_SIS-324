from repositories.user_repository import UserRepository
from models.user import User

class UserController:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username, password):
        user = User(user_id=None, username=username, password=password)
        self.user_repository.add_user(user)

    def login_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        return user and user.password == password
