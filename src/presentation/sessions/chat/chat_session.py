#pylint: disable=trailing-comma-tuple
from src.domain.models.chat import Chat
from src.presentation.interface.session_interface import SessionInterface


class ChatSession(SessionInterface):

    def __init__(self, device_id: str, session_id: str, action: str, chat: Chat):
        self.device_id = device_id
        self.session_id = session_id
        self.action = action
        self.chat = chat

    def package(self):
        response = {
            "device_id": self.device_id,
            "session_id": self.session_id,
            "action": self.action,
            "payload": {
                "group_id": self.chat.group_id,
                "token": self.chat.token,
                "message": self.chat.message
            }
        }

        return response