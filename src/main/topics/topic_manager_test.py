from src.main.topics.topic_manager import TopicManager
from src.domain.models.sessions import Session


def test_call_service_login():
    login_mock = {
        "username": "Vinicius Marques de Oliveira",
        "password": "Gr@ndeLu@2013Gr@ndeLu@",
    }
    session_mock = Session("esp8266_01", "sessionid_6xbdsruj2", "login", login_mock)

    topic_manager = TopicManager()
    response = topic_manager.call_service(session_mock)

    assert response["session_id"] == session_mock.session_id[0]
    assert response["action"] == session_mock.action[0]
    assert response["payload"]["username"] == login_mock["username"]
