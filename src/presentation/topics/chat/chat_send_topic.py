from src.domain.models.chat import Chat
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.chat.chat_send import ChatSend


class ChatSendTopic(TopicInterface):

    def __init__(self, use_case: ChatSend) -> None:
        self.__use_case = use_case

    def handle(self, _input: Chat) -> any:
        response = self.__use_case.chat_send(_input)
        return response
