import json
from src.domain.models.group import Group
from src.domain.use_cases.group.group_join import GroupJoinInterface
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class GroupJoin(GroupJoinInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def group_join(self, obj_group: dict) -> Group:

        token = obj_group.get("token")
        group_id = obj_group.get("group_id")

        params = json.dumps({
            'token': token,
            'group_id': group_id
        })
        self.__logger.log_session(session=params, action="group_join")
        json_data = self.__central_conn.request(params=params, action="/group/join")
        group_join = Group(group_id=json_data['payload']['group_id'],
                           group_name=json_data['payload']['group_title'])
        return group_join
