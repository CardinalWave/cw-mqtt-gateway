#pylint: disable=trailing-comma-tuple,redefined-outer-name
from unittest.mock import patch
import pytest
from src.domain.models.users import User
from src.domain.models.login import Login
from src.presentation.topics.user_login_topic import UserLoginTopic
from src.test.data.mocks.user_login import UserLoginSpy


@pytest.fixture
def mock_user():
    return User(token="6c5-9d2a-10f9159b09ee39721cd4-6f50-4", username='Lua')


@pytest.fixture
def mock_login():
    return Login(email="lua@outlook.com", password='password')


# @patch("src.data.use_cases.user_login.UserLogin.login")
def test_handle_login(mock_login, mock_user):
    login = Login(email=mock_login.email, password=mock_login.password)
    mock_login.return_value = mock_user

    use_case = UserLoginSpy()

    user_login_channel = UserLoginTopic(use_case)
    response = user_login_channel.handle(login)

    assert isinstance(response, User)
    assert response.token == mock_user.token
    assert response.username == mock_user.username
