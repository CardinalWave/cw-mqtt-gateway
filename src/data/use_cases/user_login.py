import json
import http.client
from src.domain.use_cases.user_login import UserLogin as UserLoginInterface
from src.domain.models.users import User
from src.domain.models.login import Login
from src.config.config import Config

class UserLogin(UserLoginInterface):
    cw_central_service = Config.CW_CENTRAL_SERVICE

    @classmethod
    def login(cls, login: Login) -> User:
        instnace = cls()
        return instnace._request_central(login=login)

    def _request_central(self, login: Login) -> User:
        try:
            url = self.cw_central_service
            headers = {
                'Content-type': 'application/json'
            }

            params = json.dumps({
                'email': login.email,
                'password': login.password
            })
            conn = http.client.HTTPConnection(url)
            conn.request("POST", "/user/login", params, headers)
            response = conn.getresponse()
            if response.status != 200:
                raise ValueError("Login return error")

            data = response.read()
            json_data = json.loads(data)
            conn.close()

            return User(token=json_data['token'][0], username=json_data['username'])
        except Exception as error:
            raise ValueError(f"Login error {error}") from error
