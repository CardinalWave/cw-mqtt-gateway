class Chat:

    def __init__(self, token: str, group_id=None, message=None):
        self.token = token
        self.group_id = group_id
        self.message = message

    def to_dict(self) -> dict[str, str]:
        return {
            "token": self.token,
            "group_id": self.group_id,
            "message": self.message
        }
