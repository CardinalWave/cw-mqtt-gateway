# pylint: disable=trailing-comma-tuple
from src.domain.models.users import User
from src.domain.models.login import Login
from src.presentation.topics.user_login_topic import UserLoginTopic
from src.data.use_cases.user_login import UserLogin


def test_handle():
    mock_login = Login("Lua", "password")

    use_case = UserLogin()

    user_login_channel = UserLoginTopic(use_case)
    response = user_login_channel.handle(mock_login)

    assert isinstance(response, User)
    assert response.username == mock_login.username[0]
