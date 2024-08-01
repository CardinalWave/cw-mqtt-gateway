#pylint: disable=trailing-comma-tuple


class User:
    def __init__(self, token: str, username: str, email: str) -> None:
        self.token = token
        self.username = username
        self.email = email
