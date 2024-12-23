# Imagem base do Python na versao 3.11
FROM cardinal_wave-python-base-image

#COPY requirements.txt .

#RUN apk add --no-cache git build-base libffi-dev

#RUN pip install -r requirements.txt

COPY  . /app

WORKDIR /app

ENV MQTT_BROKER_IP=mqtt-mosquitto
ENV MQTT_BROKER_PORT=1883
ENV CW_MQTT_GATEWAY_SERVICE=cw-mqtt-gateway
ENV CW_MQTT_GATEWAY=cw-mqtt-gateway
ENV CW_MQTT_GATEWAY_IP=cw-mqtt-gateway
ENV CW_MQTT_GATEWAY_PORT=5000
ENV CW_CENTRAL_SERVICE=cw-central-service
ENV CW_CENTRAL_SERVICE_IP=cw-central-service
ENV CW_CENTRAL_SERVICE_PORT=5001
ENV CW_LOG_TRACE=cw-log-trace
ENV CW_LOG_TRACE_IP=cw-log-trace
ENV CW_LOG_TRACE_PORT=5050

EXPOSE 5000

CMD [ "python", "run.py" ]
