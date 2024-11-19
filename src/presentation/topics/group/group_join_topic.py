from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_join import GroupJoinInterface


class GroupJoinTopic(TopicInterface):

    def __init__(self, use_case: GroupJoinInterface, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: dict) -> any:
        self.__logger.log_session(session=[_input.get('token'),
                                           _input.get('group_id')],
                                  action="group_join_topic")
        response = self.__use_case.group_join(_input)
        return response
