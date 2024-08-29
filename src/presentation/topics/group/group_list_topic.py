from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_list import GroupList


class GroupListTopic(TopicInterface):

    def __init__(self, use_case: GroupList) -> None:
        self.__use_case = use_case

    def handle(self, _input: str) -> any:
        response = self.__use_case.group_list(_input)
        return response
