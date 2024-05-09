#pylint: disable=trailing-comma-tuple
from src.domain.models.users import User
from src.domain.models.sessions import Session
from src.presentation.interface.session_interface import SessionInterface

class UserSession(SessionInterface):

    def __init__(self, session_id: str, action: str, user: User) -> Session:
        self.session_id = session_id,
        self.action = action,
        self.user = user

    def package(self):
        Session(self.session_id, self.action, self.user)
        response = {
                        "session_id": self.session_id[0],
                        "action": self.action[0],
                        "payload": {
                            "token": self.user.token[0],
                            "username": self.user.username
                        }
                    }

        return response
