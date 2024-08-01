from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.group.group_create import GroupCreate
from src.presentation.topics.group.group_create_topic import GroupCreateTopic
from src.presentation.sessions.group.group_session import GroupSession


def group_create_composer(device_id: str, session_id: str, action: str, obj_group: any):
    central_conn = CentralConn()
    use_case = GroupCreate(central_conn)
    topic = GroupCreateTopic(use_case)
    group = topic.handle(obj_group)
    response = GroupSession(device_id=device_id,
                            session_id=session_id,
                            action=action,
                            group=group).package()
    return response
