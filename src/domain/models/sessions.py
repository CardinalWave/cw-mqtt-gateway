#pylint: disable=trailing-comma-tuple

class Session:
    def __init__(self, session_id: str, action: str, payload: any) -> None:
        self.session_id = session_id,
        self.action = action,
        self.payload = payload
