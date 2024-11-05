from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.user.user_register import UserRegister
from src.presentation.topics.user.user_register_topic import UserRegisterTopic
from src.presentation.sessions.user.user_session import UserSession


def user_register_composer(device_id: str, session_id: str, action: str, register: any):
    central_conn = CentralConn()
    use_case = UserRegister(central_conn)
    topic = UserRegisterTopic(use_case)
    user = topic.handle(register)
    session = UserSession(session_id=session_id,
                          device_id=device_id,
                          action=action,
                          user=user).package()
    return session
