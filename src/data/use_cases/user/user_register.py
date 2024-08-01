import json
from src.domain.models.register import Register
from src.domain.use_cases.user.user_register import UserRegister as UserRegisterInterface
from src.domain.use_cases.central.central_conn import CentralConn


class UserRegister(UserRegisterInterface):

    def __init__(self, central_conn: CentralConn):
        self.__central_conn = central_conn

    def register(self, register: Register) -> None:
        params = json.dumps({
            "email": register.email,
            "username": register.username,
            "password": register.password
        })
        self.__central_conn.request(params=params, action="/user/register")
