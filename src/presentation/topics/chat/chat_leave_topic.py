from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.chat.chat_leave import ChatLeave


class ChatLeaveTopic(TopicInterface):

    def __init__(self, use_case: ChatLeave) -> None:
        self.__use_case = use_case

    def handle(self, _input: str) -> any:
        response = self.__use_case.chat_leave(_input)
        return response
