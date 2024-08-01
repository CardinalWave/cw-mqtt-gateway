from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.user.user_logout import UserLogout
from src.presentation.topics.user.user_logout_topic import UserLogoutTopic


def user_logout_composer(token: any):
    central_conn = CentralConn()
    use_case = UserLogout(central_conn)
    topic = UserLogoutTopic(use_case)
    topic.handle(token)
