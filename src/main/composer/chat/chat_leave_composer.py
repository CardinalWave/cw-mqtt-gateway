from src.data.use_cases.chat.chat_leave import ChatLeave
from src.data.use_cases.central.central_conn import CentralConn
from src.presentation.topics.chat.chat_leave_topic import ChatLeaveTopic


def chat_leave_composer(token: str):
    central_conn = CentralConn()
    use_case = ChatLeave(central_conn)
    topic = ChatLeaveTopic(use_case)
    topic.handle(token)
