#pylint: disable=broad-exception-raised, useless-import-alias

import json
import http.client
from src.domain.use_cases.central.central_conn import CentralConnInterface as CentralConnInterface
from src.config.config import Config
from src.main.logs.logs import Log


class CentralConn(CentralConnInterface):

    def __init__(self):
        self.__logger = Log()

    def request(self, params: any, action: str) -> any:
        ip = Config.CW_CENTRAL_SERVICE_IP
        port = int(Config.CW_CENTRAL_SERVICE_PORT)
        try:
            self.__logger.log_session(session=params, action=f'request - {action}')
            headers = {
                'Content-type': 'application/json'
            }

            print(ip, port)
            conn = http.client.HTTPConnection(host=ip, port=port)
            conn.request("POST", action, params, headers)
            conn.sock.settimeout(10)
            response = conn.getresponse()
            if response.status != 200:
                return {'error': 'valores incorretos'}
            data = response.read()
            json_data = json.loads(data)
            conn.close()
            return json_data
        except Exception as e:
            self.__logger.log_critical(error=e,
                                       message=f'Falha na requisicao [Parametros'
                                               f'= {params},'
                                          f'URL = http://{ip}:{port}/{action}]')
            raise Exception(e) from e
