from src.domain.models.login import Login
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user_login import UserLogin

class UserLoginTopic(TopicInterface):

    def __init__(self, use_case: UserLogin) -> None:
        self.__use_case = use_case

    def handle(self, _input: Login) -> str:
        response = self.__use_case.login(_input)
        return response
