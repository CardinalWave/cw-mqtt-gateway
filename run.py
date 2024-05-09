from src.main.mqtt.mqtt import mqttc

if __name__ == "__main__":
    mqttc.connect("192.168.15.69", 1883, 60)

    mqttc.subscribe("#");

    mqttc.loop_forever()
