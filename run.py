from src.main.mqtt.mqtt import mqttc, on_connect, on_message, on_publish

if __name__ == "__main__":
    mqttc.connect("192.168.15.69", 1883, 60)

    mqttc.subscribe("#");
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_publish = on_publish

    mqttc.loop_forever()
