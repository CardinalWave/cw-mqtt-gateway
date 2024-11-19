from src.domain.models.login import Login
from src.domain.models.users import User
from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user.user_login import UserLogin


class UserLoginTopic(TopicInterface):

    def __init__(self, use_case: UserLogin, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: Login) -> User:
        self.__logger.log_session(session=[_input.session_id,
                                           _input.device,
                                           _input.email],
                                  action="user_join_topic")
        response = self.__use_case.login(_input)
        return response
