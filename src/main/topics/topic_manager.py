#pylint: disable=no-else-return
from src.main.composer.user_login_composer import user_login_composer
from src.domain.models.sessions import Session
from src.domain.models.login import Login
class TopicManager:

    @staticmethod
    def call_service(session: Session):
        if "login" == session.action[0]:
            try:
                payload = session.payload
                login = Login(payload['username'], payload['password'])
                return user_login_composer(session.device_id, session.session_id[0], login)
            except Exception as exception:
                raise exception
        elif "server" == session.action[0]:
            return None
        else:
            raise ValueError("Topico desconhecido")
