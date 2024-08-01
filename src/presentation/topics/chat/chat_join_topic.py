from src.domain.models.chat import Chat
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.chat.chat_join import ChatJoin


class ChatJoinTopic(TopicInterface):

    def __init__(self, use_case: ChatJoin) -> None:
        self.__use_case = use_case

    def handle(self, _input: Chat) -> any:
        response = self.__use_case.chat_join(_input)
        return response
