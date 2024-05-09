#pylint: disable=unused-argument

import paho.mqtt.client as mqtt

from src.main.topics.topic_subscribe import TopicSubscribe
from src.main.adapters.mqtt_adapter import mqtt_adapter


def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")


def on_message(client, userdata, msg):
    topic_manager = TopicSubscribe()
    topic_manager.call_service(mqtt_adapter(msg))


def on_publish(client, userdata, result):
    print("data published \n")

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
