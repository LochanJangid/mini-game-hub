import time
import random
from src.ui.components import title, border
from src.games.base_game import Game
from typing import Dict, List, Union


class TerminalSession:
    """Encapsulates the logic and state of a single guessing round."""

    target_number: int
    user_input: str
    start_time: float
    end_time: float
    attempts: int

    def __init__(self, target_number: int) -> None:
        self.target_number = target_number
        self.user_input = 0
        self.start_time = 0.0
        self.end_time = 0.0
        self.attempts = 0

    def start(self) -> None:
        """Records the start time."""
        self.start_time = time.time()

    def check(self, user_input: int) -> None:
         """Make attempts in guessing and check them with targeted value.
            -- if not match it return False
               otherwise True.
        """

         self.attempts += 1

         if user_input < self.target_number:
             return "Too Small"
         if user_input > self.target_number:
             return "Too Big"
         
         self.end_time = time.time()
         return "Good"

    def _get_elapsed_time(self) -> float:
        """Returns total seconds of elapsed."""
        return  self.end_time - self.start_time

    def calculate_results(self) -> Dict[str, Union[int, float]]:
        """Coins Attempts, Time,  based on the session data."""
        elapsed = round(self._get_elapsed_time(), 2)
        coins = round(10 - elapsed/1000*self.attempts)
        return {
            "attempts": self.attempts,
            "time": elapsed,
            "coins": coins
            }

class TerminalUI:
    
    @staticmethod
    def display_title() -> None:
        """Display the game title."""
        title("Guess Number Game 🥸", "My eyes are on your mind 🫵.")

    @staticmethod
    def prompt_user_input() -> int: 
        while True:
            try:
                user_input = int(input(">> "))
                return user_input
            except ValueError:
                return 0



    @staticmethod
    def display_score_card(result: Dict[str, Union[int, float]]) -> None:
        """Display score card of Gamer."""
        print(border("top", 30))
        # Header - centered roughly
        print(f"┃{'🏆 Result 🏆':^28}┃")
        print(f"┃{"-"*30}┃")
        print(border("empty", 30))

        attempts_text = f" ATTEMPTS: {result['attempts']}"
        time_text = f" TIME: {result['time']}"
        coins_text = f" COINS: +{result['coins']} 🪙"

        print(f"┃{attempts_text:<30}┃")
        print(f"┃{time_text:<30}┃")
        print(f"┃{coins_text:<30}┃")

        print(border("empty", 30))
        print(border("bottom", 30))
    

class GuessingGame(Game):

    ui: TerminalUI

    def __init__(self) -> None:
        self.ui = TerminalUI()
    
    def run(self) -> None:
        """The center point which connect everything and run game."""
        self.ui.display_title()

        print("When you ready hit enter ↲.")
        session = TerminalSession(random.randint(0,100))
        input() # Start Trigger
        session.start()
        while True:
            user_input = self.ui.prompt_user_input()
            remark = session.check(user_input)
            print(remark)
            if remark=="Good":
                break

        results = session.calculate_results()
        self.coins = results["coins"]
        self.ui.display_score_card(results)

    def get_coins(self) -> int:
        return self.coins
