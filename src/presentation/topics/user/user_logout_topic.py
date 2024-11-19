from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user.user_logout import UserLogout


class UserLogoutTopic(TopicInterface):

    def __init__(self, use_case: UserLogout, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: str):
        self.__logger.log_session(session=[_input], action="user_logout_topic")
        self.__use_case.user_logout(_input)
