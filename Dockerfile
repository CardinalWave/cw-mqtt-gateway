# Imagem base do Python na versao 3.11
FROM python:3.11-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY  . /app

WORKDIR /app

# Define variáveis de ambiente para o IP e porta do MQTT
ENV MQTT_BROKER_IP=192.168.12.1
ENV MQTT_BROKER_PORT=1883

CMD [ "python", "run.py" ]