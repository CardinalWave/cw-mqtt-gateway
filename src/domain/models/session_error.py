#pylint: disable=trailing-comma-tuple
from src.presentation.interface.session_interface import SessionInterface


class SessionError(SessionInterface):
    def __init__(self, session_id: str, device_id: str, action: str, error_type: str, message: str) -> None:
        self.session_id = session_id
        self.device_id = device_id
        self.action = action
        self.error_type = error_type
        self.message = message

    def package(self):
        response = {
            "device_id": self.device_id,
            "session_id": self.session_id,
            "action": self.action,
            "payload": {
                "error": self.error_type,
                "message": self.message
            }
        }

        return response
