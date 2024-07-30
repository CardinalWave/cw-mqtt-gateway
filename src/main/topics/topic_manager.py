#pylint: disable=no-else-return
from src.main.composer.user_login_composer import user_login_composer
from src.domain.models.sessions import Session
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.domain.models.session_error import SessionError

import json

class TopicManager:

    @staticmethod
    def call_service(session: Session):
        if "login" == session.action:
            try:
                payload = session.payload
                login = Login(session_id=session.session_id,
                              device=session.device_id,
                              email=payload['email'],
                              password=payload['password'])
                return user_login_composer(session.device_id, session.session_id, login)
            except Exception as exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro no login").package()
        if "register" == session.action:
            try:
                payload = session.payload
                register = Register(username=session.payload['username'],
                                    email=session.payload['email'],
                                    password=payload['password'])
                return user_login_composer(session.device_id, session.session_id, login)
            except Exception as exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro no login").package()
        elif "server" == session.action:
            return None
        else:
            raise ValueError("Topico desconhecido")
