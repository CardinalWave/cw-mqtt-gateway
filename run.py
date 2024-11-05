import os
import time
from src.main.mqtt.mqtt import mqttc, on_connect, on_message, on_publish
from src.config.config import Config

if __name__ == "__main__":
 
    BASE_URL = Config.CW_CENTRAL_SERVICE
    MQTT_BROKER_IP = Config.MQTT_BROKER_IP
    MQTT_BROKER_PORT = Config.MQTT_BROKER_PORT
    MQTT_TIMESTAMP = Config.MQTT_TIMESTAMP

    connected = False

    while not connected:
        try:
            print(f"Connecting mqtt://{MQTT_BROKER_IP}:{MQTT_BROKER_PORT} - port_type {type(MQTT_BROKER_PORT)}")
            mqttc.connect(MQTT_BROKER_IP, MQTT_BROKER_PORT, 60)
            mqttc.subscribe("#")
            mqttc.on_connect = on_connect
            mqttc.on_message = on_message
            mqttc.on_publish = on_publish
            mqttc.loop_forever()
        except Exception as e:
            print(f"Falha na conexao: {e}")
            time.sleep(5)
