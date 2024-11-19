from src.domain.models.users import User
from src.presentation.sessions.user.user_session import UserSession

def test_user_session_package():

    user_mock = User("5ffe850e-8da6-4590-9ae6-b2c39646c79d", "Lua", "lua@email.com")

    user_session = UserSession("esp_test", "sessionid_6xbdsruj2", "test", user_mock).package()

    response_mock = {
                        'device_id': 'esp_test',
                        'session_id': 'sessionid_6xbdsruj2', 
                        'action': 'test', 
                        'payload': {
                            'token': '5ffe850e-8da6-4590-9ae6-b2c39646c79d', 
                            'username': 'Lua'
                            }
                    }

    assert user_session == response_mock
    assert user_session["session_id"] == response_mock["session_id"]
