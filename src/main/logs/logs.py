import datetime

from src.main.logs.log_handler import logger
from src.domain.models.sessions import Session


def log_session(session: Session, action: str):
    log_payload = {}
    log_payload['time'] = datetime.datetime.now()
    log_payload['service'] = "cw-message-service:ip_service:0000"
    log_payload['action'] = action
    # log_payload['payload'] = str(session)

    logger.info(log_payload)


def log_error(error, message: str):
    log_payload = {}
    log_payload['time'] = datetime.datetime.now()
    log_payload['service'] = "cw-message-service:ip_service:0000"
    log_payload['error'] = error
    log_payload['message'] = message

    logger.error(log_payload)


def log_warring(error, message: str):
    log_payload = {}
    log_payload['time'] = datetime.datetime.now()
    log_payload['service'] = "cw-message-service:ip_service:0000"
    log_payload['error'] = error
    log_payload['message'] = message

    logger.warning(log_payload)


def log_critical(error, message: str):
    log_payload = {}
    log_payload['time'] = datetime.datetime.now()
    log_payload['service'] = "cw-message-service:ip_service:0000"
    log_payload['payload'] = error
    log_payload['payload']['message'] = message

    logger.critical(log_payload)
