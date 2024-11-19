#pylint: disable=trailing-comma-tuple


class Session:
    def __init__(self, device_id: str, session_id: str, action: str, payload: any) -> None:
        self.device_id = device_id
        self.session_id = session_id
        self.action = action
        self.payload = payload

    def to_dict(self) -> str:
        session_dict = {
            'device_id': self.device_id,
            'session_id': self.session_id,
            'action': self.action,
            'payload': self.payload
        }
        return session_dict
