import configparser
import os

class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    MQTT_BROKER_IP = config.get('MQTT', 'IP')
    MQTT_BROKER_PORT = config.getint('MQTT', 'PORT')

    CW_CENTRAL_SERVICE = config['CW_CENTRAL_SERVICE']['BaseURL']

    # Sobrescrever com variáveis de ambiente, se disponíveis
    
    MQTT_BROKER_IP = os.getenv('MQTT_BROKER_IP', MQTT_BROKER_IP)
    MQTT_BROKER_PORT = os.getenv('MQTT_BROKER_PORT', MQTT_BROKER_PORT)
    
    CW_CENTRAL_SERVICE = os.getenv('CW_CENTRAL_SERVICE', CW_CENTRAL_SERVICE)
