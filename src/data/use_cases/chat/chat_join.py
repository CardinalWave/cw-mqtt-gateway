import json
from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.domain.models.chat import Chat
from src.main.logs.logs import log_session


class ChatJoin(ChatJoinInterface):

    def __init__(self, central_conn: CentralConnInterface):
        self.__central_conn = central_conn

    def chat_join(self, chat: Chat) -> any:
        params = json.dumps({
            "token": chat.token,
            "group_id": chat.group_id
        })
        log_session(session=params, action="chat_join")
        self.__central_conn.request(action="/chat/join", params=params)
