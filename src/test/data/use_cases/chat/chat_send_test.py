#pylint: disable=redefined-outer-name

from src.data.use_cases.chat.chat_send import ChatSend
from src.domain.models.chat import Chat
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy


def test_chat_send():
    obj_chat = Chat(token="token", message="Bom dia")
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    chat_send = ChatSend(logger=logger_mock, central_conn=central_conn)
    assert not chat_send.chat_send(obj_chat)
