from src.data.use_cases.group.group_leave import GroupLeave
from src.data.use_cases.central.central_conn import CentralConn
from src.presentation.topics.group.group_leave_topic import GroupLeaveTopic


def group_leave_composer(obj_group: any):

    central_conn = CentralConn()
    use_case = GroupLeave(central_conn=central_conn)
    topic = GroupLeaveTopic(use_case)
    topic.handle(obj_group)
