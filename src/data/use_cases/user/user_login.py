import json
from src.domain.use_cases.user.user_login import UserLogin as UserLoginInterface
from src.domain.models.users import User
from src.domain.models.login import Login
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class UserLogin(UserLoginInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def login(self, login: Login) -> User:
        params = json.dumps({
            'session_id': login.session_id,
            'device': login.device,
            'email': login.email,
            'password': login.password
        })
        self.__logger.log_session(session=params, action="user_login")
        json_data = self.__central_conn.request(params=params, action="/user/login")
        user = User(token=json_data['payload']['token'],
                    email=json_data['payload']['email'],
                    username=json_data['payload']['username'])
        return user
