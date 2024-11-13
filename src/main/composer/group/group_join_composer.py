from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.group.group_join import GroupJoin
from src.presentation.topics.group.group_join_topic import GroupJoinTopic
from src.presentation.sessions.group.group_session import GroupSession
from src.domain.models.group import Group


def group_join_composer(device_id: str, session_id: str, action: str, token: str, group_id: str):
    central_conn = CentralConn()
    use_case = GroupJoin(central_conn)
    topic = GroupJoinTopic(use_case)
    obj_group = dict(token=token, group_id=group_id)
    group = topic.handle(obj_group)
    response = GroupSession(device_id=device_id,
                            session_id=session_id,
                            action=action,
                            group=group).package()
    return response
