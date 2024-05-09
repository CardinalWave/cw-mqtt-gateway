from abc import ABC, abstractmethod

class SessionInterface(ABC):

    @abstractmethod
    def package(self) -> any: pass
