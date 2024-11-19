from abc import ABC, abstractmethod


class GroupLeaveInterface(ABC):

    @abstractmethod
    def group_leave(self, _input: dict): pass
