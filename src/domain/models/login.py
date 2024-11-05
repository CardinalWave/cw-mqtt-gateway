#pylint: disable=trailing-comma-tuple

class Login:
    def __init__(self, session_id: str, device: str, email: str, password: str):
        self.session_id = session_id
        self.device = device
        self.email = email
        self.password = password
