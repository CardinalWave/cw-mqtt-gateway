import json
from src.domain.use_cases.user.user_logout import UserLogout as UserLogoutInterface
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class UserLogout(UserLogoutInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def user_logout(self, token: str):
        params = json.dumps({
            "token": token
        })
        self.__logger.log_session(session=params, action="user_logout")
        self.__central_conn.request(params=params, action="/user/logout")
