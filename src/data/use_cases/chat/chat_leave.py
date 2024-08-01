import json
from src.domain.use_cases.chat.chat_leave import ChatLeave as ChatLeaveInterface
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.main.logs.logs import log_session


class ChatLeave(ChatLeaveInterface):

    def __init__(self, central_conn: CentralConnInterface):
        self.__central_conn = central_conn

    def chat_leave(self, token: str):
        params = json.dumps({
            "token": token
        })
        log_session(session=params, action="chat_leave")
        self.__central_conn.request(params=params, action="/chat/leave")
