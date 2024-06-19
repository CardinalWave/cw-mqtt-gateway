import os
import time
from src.main.mqtt.mqtt import mqttc, on_connect, on_message, on_publish
from src.config.config import Config

if __name__ == "__main__":
    
    BASE_URL = Config.CW_CENTRAL_SERVICE
    # ENV MQTT_BROKER_IP=192.168.12.1
    # ENV MQTT_BROKER_PORT=1883
    MQTT_BROKER_IP = Config.MQTT_BROKER_IP
    MQTT_BROKER_PORT = Config.MQTT_BROKER_PORT
    MQTT_TIMESTAMP = Config.MQTT_TIMESTAMP

    connected = False

    while not connected:
        try:
            mqttc.connect(MQTT_BROKER_IP, MQTT_BROKER_PORT, 60)
            mqttc.subscribe("#");
            mqttc.on_connect = on_connect
            mqttc.on_message = on_message
            mqttc.on_publish = on_publish
            mqttc.loop_forever()
        except Exception as e:
            print(f"Falha na conexao: {e}")
            time.sleep(5)
