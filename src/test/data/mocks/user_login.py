from src.domain.models.login import Login
from src.domain.models.users import User
from src.domain.use_cases.user.user_login import UserLogin as UserLoginInterface


class UserLoginSpy(UserLoginInterface):

    def login(self, login: Login) -> User:
        return User(token="6c5-9d2a-10f9159b09ee39721cd4-6f50-4",
                    username='Lua',
                    email="lua@outlook.com")
