from abc import ABC, abstractmethod
from stockticker.config import Config

class SecretsBase(ABC):
    @abstractmethod
    def __init__(self, config: Config):
        pass

    @abstractmethod
    def get(key: str):
        pass