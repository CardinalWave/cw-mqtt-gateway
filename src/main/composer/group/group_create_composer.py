from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.group.group_create import GroupCreate
from src.main.logs.logs import Log
from src.presentation.topics.group.group_create_topic import GroupCreateTopic
from src.presentation.sessions.group.group_session import GroupSession


def group_create_composer(device_id: str, session_id: str, action: str, obj_group: any):
    logger = Log()
    central_conn = CentralConn()
    use_case = GroupCreate(central_conn, logger)
    topic = GroupCreateTopic(use_case, logger)
    group = topic.handle(obj_group)
    response = GroupSession(device_id=device_id,
                            session_id=session_id,
                            action=action,
                            group=group).package()
    logger.log_session(action="group_create", session=response)
    return response
