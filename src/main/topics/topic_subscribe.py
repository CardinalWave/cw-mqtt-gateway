#pylint: disable=no-else-return
from src.main.composer.user_login_composer import user_login_composer
from src.domain.models.sessions import Session
from src.domain.models.login import Login

class TopicSubscribe:
    @staticmethod
    def call_service(session: Session):
        if "login" == session.action[0]:
            try:
                login = Login(session.payload.username[0], session.payload.password[0])
                return user_login_composer(login)
            except Exception as exception:
                raise exception
        else:
            raise ValueError("Topico desconhecido")
