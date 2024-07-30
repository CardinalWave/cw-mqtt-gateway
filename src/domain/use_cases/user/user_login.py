from abc import ABC, abstractmethod
from src.domain.models.users import User
from src.domain.models.login import Login

class UserLogin(ABC):

    @abstractmethod
    def login(self, login: Login) -> User: pass
