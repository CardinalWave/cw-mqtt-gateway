#pylint: disable=redefined-outer-name, use-dict-literal

from src.data.use_cases.group.group_join import GroupJoin
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy


def test_group_join():
    obj_group = dict(token="token", group_id="group_id")
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    group_join = GroupJoin(logger=logger_mock, central_conn=central_conn)
    obj_return = group_join.group_join(obj_group)
    assert obj_return.title == 'Admin Group'
    assert obj_return.group_id == '1'
