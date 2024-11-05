import json
from src.domain.use_cases.user.user_logout import UserLogout as UserLogoutInterface
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.main.logs.logs import log_session


class UserLogout(UserLogoutInterface):

    def __init__(self, central_conn: CentralConnInterface):
        self.__central_conn = central_conn

    def user_logout(self, token: str):
        params = json.dumps({
            "token": token
        })
        log_session(session=params, action="user_logout")
        self.__central_conn.request(params=params, action="/user/logout")
