#pylint: disable=trailing-comma-tuple

class Topic():
    def __init__(self, esp_id: str, session_id: str, action: str, payload: any) -> None:
        self.esp_id = esp_id,
        self.session_id = session_id,
        self.action = action,
        self.payload = payload
