from abc import ABC, abstractmethod


class CentralConnInterface(ABC):

    @abstractmethod
    def request(self, params: any, action: str) -> any: pass
