import json
from src.domain.use_cases.group.group_leave import GroupLeaveInterface
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class GroupLeave(GroupLeaveInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def group_leave(self, _input: dict):
        token = _input.get("token")
        group_id = _input.get("group_id")

        params = json.dumps({
            "token": token,
            "group_id": group_id
        })
        self.__logger.log_session(session=params, action="group_leave")
        self.__central_conn.request(action="/group/leave", params=params)
