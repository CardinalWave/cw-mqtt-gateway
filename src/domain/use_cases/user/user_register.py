from abc import ABC, abstractmethod
from src.domain.models.register import Register


class UserRegister(ABC):

    @abstractmethod
    def register(self, register: Register) -> any: pass
