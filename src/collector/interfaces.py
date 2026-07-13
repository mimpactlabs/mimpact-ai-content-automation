from abc import ABC, abstractmethod


class CollectorInterface(ABC):

    @abstractmethod
    def validate(self, url: str) -> bool:
        pass

    @abstractmethod
    def collect(self, url: str):
        pass
