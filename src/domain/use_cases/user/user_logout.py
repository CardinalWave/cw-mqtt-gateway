from abc import ABC, abstractmethod


class UserLogout(ABC):

    @abstractmethod
    def user_logout(self, token: str): pass
