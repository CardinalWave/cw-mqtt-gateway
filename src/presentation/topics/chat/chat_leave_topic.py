from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.chat.chat_leave import ChatLeave


class ChatLeaveTopic(TopicInterface):

    def __init__(self, use_case: ChatLeave, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: str) -> any:
        self.__logger.log_session(session="token " + _input,
                                  action="chat_leave_topic")
        response = self.__use_case.chat_leave(_input)
        return response
