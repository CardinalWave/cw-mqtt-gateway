from abc import ABC, abstractmethod
from src.domain.models.chat import Chat


class ChatJoin(ABC):

    @abstractmethod
    def chat_join(self, chat: Chat) -> any: pass
