#pylint: disable=unused-argument
import json
import paho.mqtt.client as mqtt
from src.main.topics.topic_manager import TopicManager
from src.main.adapters.mqtt_adapter import mqtt_adapter


def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")


def on_message(client, userdata, msg):
    topic_manager = TopicManager()
    response = topic_manager.call_service(mqtt_adapter(msg))
    json_payload = json.dumps(response)
    if json_payload is not None and response is not None:
        session_id = response["session_id"]
        action = response["action"]
        response = response["device_id"]
        topic = f"/server/{session_id}/{action}"
        client.publish(topic, json_payload)


def on_publish(client, userdata, result):
    # print("data published \n")
    pass


mqttc = mqtt.Client()
