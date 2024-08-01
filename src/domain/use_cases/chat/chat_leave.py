from abc import ABC, abstractmethod


class ChatLeave(ABC):

    @abstractmethod
    def chat_leave(self, token: str): pass
