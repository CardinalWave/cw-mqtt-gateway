import json
from src.domain.models.chat import Chat
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.main.logs.logs import log_session


class ChatSend(ChatSendInterface):

    def __init__(self, central_conn: CentralConnInterface):
        self.__central_conn = central_conn

    def chat_send(self, chat: Chat):
        params = json.dumps({
            "token": chat.token,
            "message": chat.message
        })
        log_session(session=params, action="chat_send")
        self.__central_conn.request(params=params, action="/chat/send")
