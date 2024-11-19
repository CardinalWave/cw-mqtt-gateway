from src.domain.models.group import Group
from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.group.group_create import GroupCreate


class GroupCreateTopic(TopicInterface):

    def __init__(self, use_case: GroupCreate, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: Group) -> any:
        self.__logger.log_session(session=[_input.group_id,
                                           _input.title],
                                  action="group_create_topic")
        response = self.__use_case.group_create(_input)
        return response
