# pylint: disable=missing-function-docstring
import uuid
from src.domain.use_cases.user_login import UserLogin as UserLoginInterface
from src.domain.models.users import User
from src.domain.models.login import Login


class UserLogin(UserLoginInterface):
    @classmethod
    def login(cls, login: Login) -> User:
        token = str(uuid.uuid4())
        response = User(token, login.username[0])
        return response
