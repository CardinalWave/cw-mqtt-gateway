from abc import ABC, abstractmethod
from src.domain.models.chat import Chat


class ChatSend(ABC):

    @abstractmethod
    def chat_send(self, chat: Chat): pass
