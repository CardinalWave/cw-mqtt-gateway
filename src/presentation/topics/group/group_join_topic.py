from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_join import GroupJoin


class GroupJoinTopic(TopicInterface):

    def __init__(self, use_case: GroupJoin) -> None:
        self.__use_case = use_case

    def handle(self, _input: dict) -> any:
        response = self.__use_case.group_join(_input)
        return response
