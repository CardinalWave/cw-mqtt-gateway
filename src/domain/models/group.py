class Group:

    def __init__(self, group_name, group_id=None):
        self.group_id = group_id
        self.title = group_name

    def to_dict(self) -> dict[str, str]:
        return {
            "group_id": self.group_id,
            "title": self.title
        }
