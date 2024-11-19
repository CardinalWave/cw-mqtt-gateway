#pylint: disable=redefined-outer-name, assignment-from-no-return

from src.data.use_cases.chat.chat_join import ChatJoin
from src.domain.models.chat import Chat
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy


def test_chat_join():
    obj_chat = Chat(token="token", group_id="group_id")
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    chat_join = ChatJoin(logger=logger_mock, central_conn=central_conn)
    obj_return = chat_join.chat_join(obj_chat)
    assert not obj_return
