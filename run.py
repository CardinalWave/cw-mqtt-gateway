import os
import time
from src.main.mqtt.mqtt import mqttc, on_connect, on_message, on_publish

if __name__ == "__main__":

    # ENV MQTT_BROKER_IP=192.168.12.1
    # ENV MQTT_BROKER_PORT=1883
    mqtt_broker_ip = '192.168.15.69'
    mqtt_broker_port = int(1883)

    connected = False

    while not connected:
        try:
            mqttc.connect(mqtt_broker_ip, mqtt_broker_port, 60)
            mqttc.subscribe("#");
            mqttc.on_connect = on_connect
            mqttc.on_message = on_message
            mqttc.on_publish = on_publish
            mqttc.loop_forever()
        except Exception as e:
            print(f"Falha na conexao: {e}")
            time.sleep(5)
