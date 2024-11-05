from src.domain.models.group import Group
from src.domain.models.users import User
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_create import GroupCreate


class GroupCreateTopic(TopicInterface):

    def __init__(self, use_case: GroupCreate) -> None:
        self.__use_case = use_case

    def handle(self, _input: Group) -> any:
        response = self.__use_case.group_create(_input)
        return response
