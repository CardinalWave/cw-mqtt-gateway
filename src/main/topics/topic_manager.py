#pylint: disable=no-else-return
from src.main.composer.user.user_login_composer import user_login_composer
from src.main.composer.user.user_register_composer import user_register_composer
from src.main.composer.user.user_logout_composer import user_logout_composer
from src.main.composer.group.group_create_composer import group_create_composer
from src.main.composer.group.group_list_composer import group_list_composer
from src.main.composer.group.group_join_composer import group_join_composer
from src.main.composer.group.group_leave_composer import group_leave_composer
from src.main.composer.chat.chat_join_composer import chat_join_composer
from src.main.composer.chat.chat_send_composer import chat_send_composer
from src.main.composer.chat.chat_leave_composer import chat_leave_composer
from src.domain.models.chat import Chat
from src.domain.models.sessions import Session
from src.domain.models.login import Login
from src.domain.models.users import User
from src.domain.models.group import Group
from src.domain.models.register import Register
from src.domain.models.session_error import SessionError
from src.main.logs.logs import log_session, log_error

import json

class TopicManager:

    @staticmethod
    def call_service(session: Session):
        if session is None or "server" == session.action:
            return None
        log_session(session=session.to_dict(), action="call_service")
        if "login" == session.action:
            try:
                payload = session.payload
                login = Login(session_id=session.session_id,
                              device=session.device_id,
                              email=payload['email'],
                              password=payload['password'])
                return user_login_composer(session.device_id, session.session_id, session.action, login)
            except Exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro ao realizar login").package()
        elif "logout" == session.action:
            try:
                payload = session.payload
                return user_logout_composer(payload['token'])
            except Exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro ao realizar logout").package()
        elif "register" == session.action:
            try:
                payload = session.payload
                register = Register(username=payload['username'],
                                    email=payload['email'],
                                    password=payload['password'])
                return user_register_composer(session.device_id, session.session_id, session.action, register)
            except Exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro ao registrar usuario").package()
        elif "group_create" == session.action:
            try:
                payload = session.payload
                group = Group(payload['title'])
                return group_create_composer(session.device_id, session.session_id, session.action, group)
            except Exception as error:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type=str(error),
                                    message="Erro ao registrar grupo").package()
        elif "group_list" == session.action:
            try:
                payload = session.payload
                token = payload['token']
                return group_list_composer(session.session_id, session.device_id, session.action, token)
            except Exception as error:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type=str(error),
                                    message="Erro ao listar grupos").package()
        elif "group_join" == session.action:
            try:
                payload = session.payload
                request = (payload['token'], payload["group_id"])
                return group_join_composer(session.device_id, session.session_id, session.action, request)
            except Exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro ao se inscrever").package()
        elif "group_leave" == session.action:
            try:
                payload = session.payload
                request = (payload['token'], payload["group_id"])
                group_leave_composer(request)
            except Exception:
                return SessionError(session_id=session.session_id,
                                    device_id=session.device_id,
                                    action=session.action,
                                    error_type="Params",
                                    message="Erro ao se inscrever").package()
        elif "chat_join" == session.action:
            try:
                log_session(session=session.to_dict(), action=session.action)
                payload = session.payload
                request = Chat(group_id=payload["group_id"], token=payload["token"])
                chat_join_composer(request)
            except Exception as error:
                session_error = SessionError(session_id=session.session_id,
                                             device_id=session.device_id,
                                             action=session.action,
                                             error_type=str(error),
                                             message="Erro ao entrar no chat").package()
                log_error(error=session_error, message=session_error['payload'])
                return session_error

        elif "chat_send" == session.action:
            try:
                log_session(session=session.to_dict(), action=session.action)
                payload = session.payload
                request = Chat(token=payload["token"],
                               message=payload["message"])
                chat_send_composer(request)
            except Exception as error:
                session_error = SessionError(session_id=session.session_id,
                                             device_id=session.device_id,
                                             action=session.action,
                                             error_type=str(error),
                                             message="Erro ao entrar no chat").package()
                log_error(error=session_error, message=session_error['payload'])
                return session_error
        elif "chat_leave" == session.action:
            try:
                log_session(session=session.to_dict(), action=session.action)
                payload = session.payload
                chat_leave_composer(payload["token"])
            except Exception as error:
                session_error = SessionError(session_id=session.session_id,
                                             device_id=session.device_id,
                                             action=session.action,
                                             error_type=str(error),
                                             message="Erro ao sair do chat").package()
                log_error(error=session_error, message=session_error['payload'])
                return session_error

        else:

            raise ValueError("Topico desconhecido")
