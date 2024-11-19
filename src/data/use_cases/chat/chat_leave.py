import json
from src.domain.use_cases.chat.chat_leave import ChatLeave as ChatLeaveInterface
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class ChatLeave(ChatLeaveInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def chat_leave(self, token: str):
        params = json.dumps({
            "token": token
        })
        self.__logger.log_session(session=params, action="chat_leave")
        self.__central_conn.request(params=params, action="/chat/leave")
