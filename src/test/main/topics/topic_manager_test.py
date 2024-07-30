#pylint: disable=redefined-outer-name, singleton-comparison
from unittest.mock import patch
from src.main.topics.topic_manager import TopicManager
from src.domain.models.sessions import Session

@patch("src.data.use_cases.user_login.UserLogin.login")
def test_call_service_login():
    login_mock = {"email":"lua@outlook.com", "password":"password"}
    session_mock = Session("esp8266_01", "sessionid_6xbdsruj2", "login", login_mock)

    topic_manager = TopicManager()
    response = topic_manager.call_service(session_mock)

    assert response["session_id"] == session_mock.session_id[0]
    assert response["action"] == session_mock.action[0]
    assert response["payload"]["token"] != None
    assert response["payload"]["username"] != None
