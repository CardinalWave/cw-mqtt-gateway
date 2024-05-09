from src.presentation.topics.user_login_topic import UserLoginTopic
from src.data.use_cases.user_login import UserLogin

def user_login_composer(login: any):

    use_case = UserLogin()
    topic = UserLoginTopic(use_case)

    return topic.handle(login)
