from src.domain.models.register import Register
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user.user_register import UserRegister


class UserRegisterTopic(TopicInterface):

    def __init__(self, use_case: UserRegister) -> None:
        self.__use_case = use_case

    def handle(self, _input: Register):
        response = self.__use_case.register(_input)
        return response
