from src.presentation.topics.user_login_topic import UserLoginTopic
from src.presentation.sessions.user_session import UserSession
from src.data.use_cases.user_login import UserLogin

def user_login_composer(device_id: str, session_id: str, login: any):
    
    use_case = UserLogin()
    topic = UserLoginTopic(use_case)
    user = topic.handle(login)
    session = UserSession(device_id, session_id, "login", user).package()

    return session
