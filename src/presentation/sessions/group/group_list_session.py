#pylint: disable=trailing-comma-tuple
from src.domain.models.group import Group
from src.presentation.interface.session_interface import SessionInterface


class GroupListSession(SessionInterface):

    def __init__(self, device_id: str, session_id: str, action: str, list_group: list[Group]):
        self.device_id = device_id
        self.session_id = session_id
        self.action = action
        self.list_group = list_group

    def package(self):
        response = {
            "device_id": self.device_id,
            "session_id": self.session_id,
            "action": self.action,
            "payload": {
                "groups": [group.to_dict() for group in self.list_group]
            }
        }

        return response
