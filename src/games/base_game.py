from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def run(self, player: int):
        pass

    @abstractmethod
    def get_coins(self) -> float:
        pass

class GameSession(ABC):
    import time
    from typing import Dict, Union
    
    def start(self):
        self._start_time = self.time.time()

    def stop(self):
        self._end_time = self.time.time()

    def _get_elapsed_time(self) -> float:
        return self._end_time - self._start_time

    @abstractmethod
    def calculate_score(self, user_input: str) -> Dict[str, Union[int, float, str]]:
        pass

class GameUI(ABC):
    from typing import Dict, Union
    from src.ui.components import border

    @staticmethod
    @abstractmethod
    def display_title() -> None:
        pass
    
    def display_score_card(self, result: Dict[str, Union[int, float, str]]) -> None:
        """Display score card of Gamer."""
        from src.ui.components import border
        
        print(border("top", 30))
        # Header - centered roughly
        print(f"┃{'🏆 Result 🏆':^28}┃")
        print(f"┃{"-"*30}┃")
        print(border("empty", 30))

        # Data rows with dynamic padding to keep the box width consistent
        for key, value in result.items():
            print(f"┃{key.title():<15}", end="")
            print(f"{str(value):>15}┃")

        print(border("empty", 30))
        print(border("bottom", 30))
