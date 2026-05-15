from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def get_coins(self) -> int:
        pass
