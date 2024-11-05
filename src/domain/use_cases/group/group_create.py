from abc import ABC, abstractmethod
from src.domain.models.group import Group


class GroupCreate(ABC):

    @abstractmethod
    def group_create(self, group: Group) -> any: pass
