from abc import ABC, abstractmethod
from src.domain.models.group import Group


class GroupList(ABC):

    @abstractmethod
    def group_list(self, token: str) -> list[Group]: pass
