import json
from src.domain.use_cases.central.central_conn import CentralConn
from src.domain.models.group import Group
from src.domain.use_cases.group.group_create import GroupCreate as GroupCreateInterface


class GroupCreate(GroupCreateInterface):

    def __init__(self, central_conn: CentralConn):
        self.__central_conn = central_conn

    def group_create(self, group: Group) -> Group:
        params = json.dumps({
            'title': group.title
        })
        json_data = self.__central_conn.request(params=params, action="/group/create")
        response = Group(group_id=json_data['payload']['group_id'],
                         group_name=json_data['payload']['title'])
        return response
