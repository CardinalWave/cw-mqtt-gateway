import json
from src.domain.models.chat import Chat
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class ChatSend(ChatSendInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger


    def chat_send(self, chat: Chat):
        params = json.dumps({
            "token": chat.token,
            "message": chat.message
        })
        self.__logger.log_session(session=params, action="chat_send")
        self.__central_conn.request(params=params, action="/chat/send")
