from src.domain.models.users import User
from src.domain.models.login import Login
from .user_login import UserLogin

def test_login():
    mock_login = Login("Lua", "123#dasd")

    user_login = UserLogin()
    response = user_login.login(mock_login)

    assert isinstance(response, User)
    assert response.username == mock_login.username[0]
    assert response.token is not None
