#pylint: disable=redefined-outer-name
import json
from unittest.mock import Mock

import pytest
from src.domain.models.login import Login
from src.data.use_cases.user.user_login import UserLogin
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy

@pytest.fixture
def mock_login():
    return Login('sessionId', 'cloud_00', email="lua@email.com", password="12345")


def test_user_login(mock_login):
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
    user_login = UserLogin(logger=logger_mock, central_conn=central_conn)
    user = user_login.login(mock_login)
    assert user.token == 'session_id0000'
    assert user.email == 'lua@email.com'
