from src.domain.models.register import Register
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.user.user_logout import UserLogout


class UserLogoutTopic(TopicInterface):

    def __init__(self, use_case: UserLogout) -> None:
        self.__use_case = use_case

    def handle(self, _input: str):
        self.__use_case.user_logout(_input)
