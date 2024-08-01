from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.chat.chat_send import ChatSend
from src.presentation.topics.chat.chat_send_topic import ChatSendTopic


def chat_send_composer(obj_chat: any):
    central_conn = CentralConn()
    use_case = ChatSend(central_conn)
    topic = ChatSendTopic(use_case)
    topic.handle(obj_chat)