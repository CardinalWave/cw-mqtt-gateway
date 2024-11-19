#pylint: disable=trailing-comma-tuple
from src.domain.models.users import User
from src.presentation.interface.session_interface import SessionInterface


class UserSession(SessionInterface):

    def __init__(self, device_id: str, session_id: str, action: str, user: User):
        self.device_id = device_id
        self.session_id = session_id
        self.action = action
        self.user = user

    def package(self):
        response = {
            "device_id": self.device_id,
            "session_id": self.session_id,
            "action": self.action,
            "payload": {
                "token": self.user.token,
                "username": self.user.username
            }
        }

        return response
