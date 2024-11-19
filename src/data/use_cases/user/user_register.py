import json
from src.domain.models.register import Register
from src.domain.models.users import User
from src.domain.use_cases.user.user_register import UserRegister as UserRegisterInterface
from src.domain.use_cases.central.central_conn import CentralConnInterface
from src.main.logs.logs_interface import LogInterface


class UserRegister(UserRegisterInterface):

    def __init__(self, central_conn: CentralConnInterface, logger: LogInterface):
        self.__central_conn = central_conn
        self.__logger = logger

    def register(self, register: Register) -> User:
        params = json.dumps({
            "email": register.email,
            "username": register.username,
            "password": register.password
        })
        self.__logger.log_session(session=params, action="user_register")
        json_data = self.__central_conn.request(params=params, action="/user/register")
        user = User(token=json_data['payload']['token'],
                    email=json_data['payload']['email'],
                    username=json_data['payload']['username'])
        return user
