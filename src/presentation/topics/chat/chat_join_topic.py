from src.domain.models.chat import Chat
from src.main.logs.logs_interface import LogInterface
from src.presentation.interface.topic_interface import TopicInterface
from src.domain.use_cases.chat.chat_join import ChatJoin


class ChatJoinTopic(TopicInterface):

    def __init__(self, use_case: ChatJoin, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, _input: Chat) -> any:
        self.__logger.log_session(session=[_input.token,
                                           _input.group_id,
                                           _input.message],
                                  action="chat_join_topic")
        response = self.__use_case.chat_join(_input)
        return response
