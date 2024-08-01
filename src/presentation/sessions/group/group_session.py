#pylint: disable=trailing-comma-tuple
from src.domain.models.group import Group
from src.presentation.interface.session_interface import SessionInterface


class GroupSession(SessionInterface):

    def __init__(self, device_id: str, session_id: str, action: str, group: Group):
        self.device_id = device_id
        self.session_id = session_id
        self.action = action
        self.group = group

    def package(self):
        response = {
            "device_id": self.device_id,
            "session_id": self.session_id,
            "action": self.action,
            "payload": {
                "group_id": self.group.group_id,
                "title": self.group.title
            }
        }

        return response
