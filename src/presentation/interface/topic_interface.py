from abc import ABC, abstractmethod

class TopicInterface(ABC):

    @abstractmethod
    def handle(self, _input: any) -> any: pass
