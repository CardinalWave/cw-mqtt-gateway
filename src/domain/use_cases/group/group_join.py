from abc import ABC, abstractmethod


class GroupJoin(ABC):

    @abstractmethod
    def group_join(self, group_user: dict) -> any: pass
