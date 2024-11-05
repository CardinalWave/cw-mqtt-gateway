#pylint: disable=redefined-outer-name
import json
from unittest.mock import Mock
import pytest
from src.domain.models.users import User
from src.domain.models.login import Login
from src.data.use_cases.user.user_login import UserLogin
from src.config.config import Config

BASE_URL = Config.CW_CENTRAL_SERVICE


@pytest.fixture
def mock_login():
    return Login('lua@outlook.com', 'password213')


@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee", username='Lua')


def test_user_login(mock_http_conn, mock_login, mock_user):
    mock_response = Mock()
    mock_response.status = 200
    mock_response.read.return_value = json.dumps({
        'token': mock_user.token,
        'username': mock_user.username
    }).encode('utf-8')

    user = UserLogin.login(mock_login)
    assert user.token == mock_user.token
    assert user.username == mock_user.username
