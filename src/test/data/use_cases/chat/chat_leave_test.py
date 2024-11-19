#pylint: disable=redefined-outer-name

from src.data.use_cases.chat.chat_leave import ChatLeave
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy


def test_chat_leave():
    token = "token"
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    chat_leave = ChatLeave(logger=logger_mock, central_conn=central_conn)
    assert not chat_leave.chat_leave(token)
