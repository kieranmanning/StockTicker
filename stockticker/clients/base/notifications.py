from abc import ABC, abstractmethod
from stockticker.config import Config

class NotificationsBase(ABC):
    @abstractmethod
    def __init__(self, config: Config):
        pass

    @abstractmethod
    def send(message: str):
        pass