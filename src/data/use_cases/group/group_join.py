import json
from src.domain.models.group import Group
from src.domain.use_cases.group.group_join import GroupJoin as GroupJoinInterface
from src.domain.use_cases.central.central_conn import CentralConn


class GroupJoin(GroupJoinInterface):

    def __init__(self, central_conn: CentralConn):
        self.__central_conn = central_conn

    def group_join(self, group_user: dict) -> Group:

        user = group_user[1]
        group = group_user[0]

        params = json.dumps({
            'token': user.token,
            'username': user.username,
            'group_title': group.title,
            'group_id': group.group_id
        })
        print(params)
        json_data = self.__central_conn.request(params=params, action="/group/join")
        group_join = Group(group_id=json_data['payload']['group_id'],
                           group_name=json_data['payload']['group_title'])
        return group_join
