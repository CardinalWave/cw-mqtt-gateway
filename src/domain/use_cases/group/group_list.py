from abc import ABC, abstractmethod
from src.domain.models.group import Group
from src.domain.models.users import User


class GroupList(ABC):

    @abstractmethod
    def group_list(self, user: User) -> list[Group]: pass
