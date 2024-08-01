from src.data.use_cases.central.central_conn import CentralConn
from src.data.use_cases.user.user_register import UserRegister
from src.presentation.topics.user.user_register_topic import UserRegisterTopic


def user_register_composer(register: any):
    central_conn = CentralConn()
    use_case = UserRegister(central_conn)
    topic = UserRegisterTopic(use_case)
    topic.handle(register)
