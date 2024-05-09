from src.main.topics.topic_subscribe import TopicSubscribe
from src.domain.models.sessions import Session
from src.domain.models.login import Login
from src.domain.models.users import User


def test_call_service_login():

    login_mock = Login("Vinicius Marques de Oliveira", "Gr@ndeLu@2013Gr@ndeLu@")

    session_mock = Session("sessionid_6xbdsruj2", "login", login_mock)

    topic_subscribe = TopicSubscribe();
    response = topic_subscribe.call_service(session_mock)

    assert isinstance(response, User)
