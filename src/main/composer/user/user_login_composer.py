from src.presentation.topics.user.user_login_topic import UserLoginTopic
from src.presentation.sessions.user.user_session import UserSession
from src.data.use_cases.user.user_login import UserLogin
from src.data.use_cases.central.central_conn import CentralConn


def user_login_composer(device_id: str, session_id: str, action: str, login: any):
    central_conn = CentralConn()
    use_case = UserLogin(central_conn)
    topic = UserLoginTopic(use_case)
    user = topic.handle(login)
    session = UserSession(session_id=session_id,
                          device_id=device_id,
                          action=action,
                          user=user).package()

    return session
