from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_leave import GroupLeaveInterface


class GroupLeaveTopic(TopicInterface):

    def __init__(self, use_case: GroupLeaveInterface, logger: LogInterface) -> None:
        self.__logger = logger
        self.__use_case = use_case

    def handle(self, _input: dict) -> any:
        self.__logger.log_session(session=[_input.get('token'),
                                           _input.get('group_id')],
                                  action="group_leave_topic")
        response = self.__use_case.group_leave(_input)
        return response
