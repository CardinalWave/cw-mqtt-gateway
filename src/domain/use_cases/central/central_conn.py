from abc import ABC, abstractmethod


class CentralConn(ABC):

    @abstractmethod
    def request(self, params: any, action: str) -> any: pass
