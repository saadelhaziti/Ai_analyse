# Abstract class
from abc import ABC, abstractmethod
class StorageBackend(ABC):
    @abstractmethod
    def save(self, key: str, data: dict) -> None:
        pass

    @abstractmethod
    def retrieve(self, key: str) -> dict:
        pass