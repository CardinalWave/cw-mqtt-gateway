from abc import ABC, abstractmethod


class GroupLeave(ABC):

    @abstractmethod
    def group_leave(self, token: str, group_id: str): pass
