import json
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.domain.models.group import Group
from src.domain.use_cases.group.group_create import GroupCreate as GroupCreateInterface
from src.main.logs.logs_interface import LogInterface


class GroupCreate(GroupCreateInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def group_create(self, group: Group) -> Group:
        params = json.dumps({
            'title': group.title
        })
        self.__logger.log_session(session=params, action="group_create")
        json_data = self.__central_conn.request(params=params, action="/group/create")
        response = Group(group_id=json_data['payload']['group_id'],
                         group_name=json_data['payload']['title'])
        return response
