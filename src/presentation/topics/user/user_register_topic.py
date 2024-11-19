from src.domain.models.register import Register
from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user.user_register import UserRegister


class UserRegisterTopic(TopicInterface):

    def __init__(self, use_case: UserRegister, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: Register):
        self.__logger.log_session(session=[_input.email,
                                           _input.username],
                                  action="user_register_topic")
        response = self.__use_case.register(_input)
        return response
