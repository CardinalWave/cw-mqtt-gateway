#pylint: disable=redefined-outer-name
import json
from unittest.mock import Mock

import pytest

from src.data.use_cases.user.user_register import UserRegister
from src.domain.models.register import Register
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy

@pytest.fixture
def mock_register():
    return Register('lua@email.co', 'username', password="12345")


def test_user_register(mock_register):
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
    user_register = UserRegister(logger=logger_mock, central_conn=central_conn)
    user = user_register.register(mock_register)
    assert user.token == 'session_id0000'
    assert user.email == 'lua@email.com'
