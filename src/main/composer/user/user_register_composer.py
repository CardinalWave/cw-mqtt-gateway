#pylint: disable=abstract-class-instantiated
from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.user.user_register import UserRegister
from src.domain.models.register import Register
from src.main.logs.logs import Log
from src.presentation.topics.user.user_register_topic import UserRegisterTopic
from src.presentation.sessions.user.user_session import UserSession


def user_register_composer(device_id: str,
                           session_id: str,
                           action: str,
                           register: Register):

    logger = Log()
    central_conn = CentralConn()
    use_case = UserRegister(central_conn, logger)
    topic = UserRegisterTopic(use_case, logger)
    user = topic.handle(register)
    session = UserSession(session_id=session_id,
                          device_id=device_id,
                          action=action,
                          user=user).package()
    logger.log_session(action="user_register_composer", session=session)
    return session
