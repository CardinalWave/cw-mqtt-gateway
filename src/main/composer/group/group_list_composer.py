from src.data.use_cases.group.group_list import GroupList
from src.data.use_cases.central.central_conn import CentralConn
from src.presentation.sessions.group.group_list_session import GroupListSession
from src.presentation.topics.group.group_list_topic import GroupListTopic


def group_list_composer(session_id: str, device_id: str, action: str, user: any):
    central_conn = CentralConn()
    use_case = GroupList(central_conn)
    topic = GroupListTopic(use_case)
    list_group = topic.handle(user)
    session = GroupListSession(session_id=session_id,
                               device_id=device_id,
                               action=action,
                               list_group=list_group).package()

    return session
