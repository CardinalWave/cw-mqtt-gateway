#pylint: disable=redefined-outer-name
import json
from unittest.mock import Mock
from src.data.use_cases.user.user_logout import UserLogout
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy

def test_user_login():
    token = "token"
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    mock_response = Mock()
    mock_response.status = 200
    payload = json.dumps({
        'session_id': 'session_id0000',
        'device': '',
        'email': 'lua@email.com',
        'password': '12345'
    }).encode('utf-8')

    mock_response.read.return_value = payload
    user_logout = UserLogout(logger=logger_mock, central_conn=central_conn)
    assert not user_logout.user_logout(token)
