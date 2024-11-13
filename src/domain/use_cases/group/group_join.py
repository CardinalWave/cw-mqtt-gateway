from abc import ABC, abstractmethod


class GroupJoin(ABC):

    @abstractmethod
    def group_join(self, obj_group: dict) -> any: pass
