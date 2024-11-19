#pylint: disable=redefined-outer-name, literal-comparison
from src.data.use_cases.group.group_create import GroupCreate
from src.domain.models.group import Group
from src.test.main.mocks.central_conn import CentralConnSpy
from src.test.main.mocks.logs import LogSpy


def test_group_create():
    group_mock = Group(group_id='GroupId', group_name="GroupName")
    logger_mock = LogSpy()
    central_conn = CentralConnSpy()
    group_create = GroupCreate(logger=logger_mock, central_conn=central_conn)
    group_return = group_create.group_create(group_mock)
    assert group_return.group_id == "1"
    assert group_return.title == 'Admin Group'
