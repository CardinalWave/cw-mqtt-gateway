import json
import http.client
from typing import Any
from src.config.config import Config
from src.domain.use_cases.central.central_conn import CentralConn as CentralConnInterface
from src.main.logs.logs import log_critical


class CentralConn(CentralConnInterface):
    def __init__(self):
        self.__url = Config.CW_CENTRAL_SERVICE

    def request(self, params: any, action: str) -> any:
        try:
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
            raise Exception(e) from e
