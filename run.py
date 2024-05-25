import os
import time
from src.main.mqtt.mqtt import mqttc, on_connect, on_message, on_publish

if __name__ == "__main__":

    mqtt_broker_ip = os.getenv('MQTT_BROKER_IP')
    mqtt_broker_port = int(os.getenv('MQTT_BROKER_PORT'))

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
