#pylint: disable=trailing-comma-tuple
from src.domain.models.users import User
from src.domain.models.sessions import Session
from src.presentation.interface.session_interface import SessionInterface

class UserSession(SessionInterface):

    def __init__(self, device_id: str, session_id: str, action: str, user: User) -> Session:
        self.device_id = device_id,
        self.session_id = session_id,
        self.action = action,
        self.user = user

    def package(self):
        Session(self.device_id, self.session_id, self.action, self.user)
        response = {
                        "device_id": self.device_id[0][0],
                        "session_id": self.session_id[0],
                        "action": self.action[0],
                        "payload": {
                            "token": self.user.token[0],
                            "username": self.user.username
                        }
                    }

        return response
