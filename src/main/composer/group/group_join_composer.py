#pylint: disable=use-dict-literal
from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.group.group_join import GroupJoin
from src.main.logs.logs import Log
from src.presentation.topics.group.group_join_topic import GroupJoinTopic
from src.presentation.sessions.group.group_session import GroupSession


def group_join_composer(device_id: str,
                        session_id: str,
                        action: str,
                        token: str,
                        group_id: str):
    logger = Log()
    central_conn = CentralConn()
    use_case = GroupJoin(central_conn, logger)
    topic = GroupJoinTopic(use_case, logger)
    obj_group = dict(token=token, group_id=group_id)
    group = topic.handle(obj_group)
    response = GroupSession(device_id=device_id,
                            session_id=session_id,
                            action=action,
                            group=group).package()
    logger.log_session(action="group_join", session=response)
    return response
