import json
from src.domain.use_cases.group.group_leave import GroupLeave as GroupLeaveInterface
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.main.logs.logs import log_session


class GroupLeave(GroupLeaveInterface):

    def __init__(self, central_conn: CentralConnInterface):
        self.__central_conn = central_conn

    def group_leave(self, token: str, group_id: str):
        params = json.dumps({
            "token": token,
            "group_id": group_id
        })
        log_session(session=params, action="group_leave")
        self.__central_conn.request(action="/group/leave", params=params)
