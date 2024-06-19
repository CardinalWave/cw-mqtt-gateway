import pytest
import json
from unittest.mock import patch, Mock
from src.domain.models.users import User
from src.domain.models.login import Login
from src.data.use_cases.user_login import UserLogin
from src.config.config import Config

BASE_URL = Config.CW_CENTRAL_SERVICE

@pytest.fixture
def mock_login():
    return Login('lua@outlook.com', 'password213')

@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee", username='Lua')

@patch("http.client.HTTPConnection")
def test_user_login(mock_http_conn, mock_login, mock_user):
    mock_response = Mock()
    mock_response.status = 200
    mock_response.read.return_value = json.dumps({
        'token': mock_user.token,
        'username': mock_user.username
    }).encode('utf-8')

    mock_conn_instance = mock_http_conn.return_value
    mock_conn_instance.getresponse.return_value = mock_response

    user = UserLogin.login(mock_login)
    assert user.token[0] == mock_user.token[0]
    assert user.username == mock_user.username

    mock_http_conn.assert_called_once_with(BASE_URL)
    mock_conn_instance.request.assert_called_once_with(
        "POST", 
        "/user/login", 
        json.dumps({
            'email': mock_login.email,
            'password': mock_login.password
        }), 
        {'Content-type': 'application/json'}
    )
