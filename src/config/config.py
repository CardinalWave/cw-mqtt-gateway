import configparser
import os


class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    MQTT_BROKER_IP = config.get('MQTT', 'IP')
    MQTT_BROKER_PORT = config.getint('MQTT', 'PORT')
    MQTT_TIMESTAMP = os.getenv('MQTT', 'MQTT_TIMESTAMP')
    CW_CENTRAL_SERVICE = config['CW_CENTRAL_SERVICE']['BaseURL']
    CW_CENTRAL_SERVICE_IP = config['CW_CENTRAL_SERVICE']['IP']
    CW_CENTRAL_SERVICE_PORT = config['CW_CENTRAL_SERVICE']['PORT']
    CW_LOG_TRACE = config['CW_LOG_TRACE']['BaseURL']
    CW_LOG_TRACE_IP = config['CW_LOG_TRACE']['IP']
    CW_LOG_TRACE_PORT = config['CW_LOG_TRACE']['PORT']

    # From Dockerfile
    MQTT_BROKER_IP = os.getenv('MQTT_BROKER_IP', MQTT_BROKER_IP)
    MQTT_BROKER_PORT = os.getenv('MQTT_BROKER_PORT', MQTT_BROKER_PORT)
    MQTT_TIMESTAMP = os.getenv('MQTT_TIMESTAMP', MQTT_TIMESTAMP)

    CW_CENTRAL_SERVICE = os.getenv('CW_CENTRAL_SERVICE', CW_CENTRAL_SERVICE)
