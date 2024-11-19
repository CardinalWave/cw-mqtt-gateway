from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_list import GroupList


class GroupListTopic(TopicInterface):

    def __init__(self, use_case: GroupList, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: str) -> any:
        self.__logger.log_session(session=[_input],
                                  action="group_list_topic")
        response = self.__use_case.group_list(_input)
        return response
