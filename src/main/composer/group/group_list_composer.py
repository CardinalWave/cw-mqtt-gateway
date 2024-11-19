from src.data.use_cases.group.group_list import GroupList
from src.data.use_cases.central.central_conn import CentralConn
from src.main.logs.logs import Log
from src.presentation.sessions.group.group_list_session import GroupListSession
from src.presentation.topics.group.group_list_topic import GroupListTopic


def group_list_composer(session_id: str, device_id: str, action: str, token: any):
    logger = Log()
    central_conn = CentralConn()
    use_case = GroupList(central_conn, logger)
    topic = GroupListTopic(use_case, logger)
    list_group = topic.handle(token)
    session = GroupListSession(session_id=session_id,
                               device_id=device_id,
                               action=action,
                               list_group=list_group).package()
    logger.log_session(action="group_list", session=session)
    return session
