import json
import http.client
from src.config.config import Config
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.main.logs.logs import log_critical, log_session


class CentralConn(CentralConnInterface):
    def __init__(self):
        self.__url = Config.CW_CENTRAL_SERVICE

    def request(self, params: any, action: str) -> any:
        try:
            log_session(session=params, action=f'request - {action}')
            headers = {
                'Content-type': 'application/json'
            }
            conn = http.client.HTTPConnection(host='192.168.15.69', port=5000)
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
            log_critical(error=e, message=f'Falha na requisicao [Parametros = {params},'
                                          f'URL = http://192.168.15.69:5000/{action}]')
            raise Exception(e) from e
