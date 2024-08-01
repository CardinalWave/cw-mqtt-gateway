import json
from src.domain.use_cases.central.central_conn import CentralConn
from src.domain.models.group import Group
from src.domain.use_cases.group.group_list import GroupList as GroupListInterface
from src.domain.models.users import User


class GroupList(GroupListInterface):

    def __init__(self, central_conn: CentralConn):
        self.__central_conn = central_conn

    def group_list(self, user: User) -> list[Group]:
        params = json.dumps({
            'token': user.token,
            'email': user.email,
            'username': user.username
        })
        json_data = self.__central_conn.request(params=params, action="/group/list")
        formated_group_list = self.__format_list(json_list=json_data['payload'])
        return formated_group_list

    @staticmethod
    def __format_list(json_list: []):
        list_group = []
        for group in json_list:
            group_item = Group(group_name=group['title'], group_id=group['group_id'])
            list_group.append(group_item)
        return list_group
