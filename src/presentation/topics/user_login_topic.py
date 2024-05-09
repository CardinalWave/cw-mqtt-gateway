from src.domain.models.users import User
from src.domain.models.login import Login
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user_login import UserLogin
import json

class UserLoginTopic(TopicInterface):

    def __init__(self, use_case: UserLogin) -> None:
        self.__use_case = use_case

    def handle(self, _input: Login) -> User:
        response = self.__use_case.login(_input)
        json_str = json.dumps(response.__dict__)
        print(json_str)
        return response
