from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.chat.chat_join import ChatJoin
from src.presentation.topics.chat.chat_join_topic import ChatJoinTopic


def chat_join_composer(obj_chat: any):
    central_conn = CentralConn()
    use_case = ChatJoin(central_conn)
    topic = ChatJoinTopic(use_case)
    topic.handle(obj_chat)