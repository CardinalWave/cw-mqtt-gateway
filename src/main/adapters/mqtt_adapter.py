import json
from src.domain.models.sessions import Session

def mqtt_adapter(msg: any) -> any:

    parts = msg.topic.split('/')

    payload_obj = json.loads(msg.payload.decode("utf-8"))

    device_id = parts[1]
    session_id = parts[2]
    action = parts[3]
    payload = payload_obj['payload']

    if device_id == "server":
        action = "server"

    session = Session(device_id, session_id, action, payload)

    return session
