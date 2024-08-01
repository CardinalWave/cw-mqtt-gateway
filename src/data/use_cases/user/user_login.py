import json
from src.domain.use_cases.user.user_login import UserLogin as UserLoginInterface
from src.domain.models.users import User
from src.domain.models.login import Login
from src.config.config import Config
from src.domain.use_cases.central.central_conn import CentralConn
from src.main.logs.logs import log_session


class UserLogin(UserLoginInterface):
    cw_central_service = Config.CW_CENTRAL_SERVICE

    def __init__(self, central_conn: CentralConn):
        self.__central_conn = central_conn

    def login(self, login: Login) -> User:
        params = json.dumps({
            'session_id': login.session_id,
            'device': login.device,
            'email': login.email,
            'password': login.password
        })
        log_session(session=params, action="user_login")
        json_data = self.__central_conn.request(params=params, action="/user/login")
        user = User(token=json_data['payload']['token'],
                    email=json_data['payload']['email'],
                    username=json_data['payload']['username'])
        return user
