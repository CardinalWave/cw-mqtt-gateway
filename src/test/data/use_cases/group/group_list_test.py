#pylint: disable=redefined-outer-name
import json
from unittest.mock import Mock


from src.data.use_cases.group.group_list import GroupList
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy


def test_group_list():
    token = "token"
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    mock_response = Mock()
    mock_response.status = 200
    payload = json.dumps({
        'session_id': 'session_id0000',
        'device': '',
        'email': 'lua@email.com',
        'password': '12345'
    }).encode('utf-8')

    mock_response.read.return_value = payload
    group_list = GroupList(logger=logger_mock, central_conn=central_conn)
    list_return = group_list.group_list(token)
    assert len(list_return) > 0
