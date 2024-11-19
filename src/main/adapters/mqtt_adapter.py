#pylint: disable=inconsistent-return-statements

import json
from src.domain.models.sessions import Session


def mqtt_adapter(msg: any) -> any:
    parts = msg.topic.split('/')
    payload_obj = json.loads(msg.payload.decode("utf-8"))
    print(parts)
    device_id = parts[1]
    session_id = parts[2]
    action = parts[3]
    payload = payload_obj['payload']

    if device_id == "server":
        return

    session = Session(device_id, session_id, action, payload)

    return session
