import random
from src.ui.components import box
from src.games.base_game import Game, GameUI, GameSession
from src.db.models import save_score
from typing import Dict, Union


class TerminalSession(GameSession):
    """Encapsulates the logic and state of a single guessing round."""

    target_number: int
    user_input: str
    attempts: int

    def __init__(self, target_number: int) -> None:
        self.target_number = target_number
        self.user_input = ''
        self.start_time = 0.0
        self.end_time = 0.0
        self.attempts = 0

    def check(self, user_input: int) -> str:
         """Make attempts in guessing and check them with targeted value.
            -- if not match it return False
               otherwise True.
        """

         self.attempts += 1

         if user_input < self.target_number:
             return "Too Small"
         if user_input > self.target_number:
             return "Too Big"
             
         return "Good"

    def calculate_score(self, user_input: str) -> Dict[str, Union[int, float, str]]:
        """Coins Attempts, Time,  based on the session data."""
        self.stop()
        elapsed = round(self._get_elapsed_time(), 2)
        coins = round(10 - elapsed/1000*self.attempts)
        return {
            "attempts": self.attempts,
            "time": elapsed,
            "coins": coins
            }

class TerminalUI(GameUI):
    
    @staticmethod
    def display_title() -> None:
        """Display the game title."""
        box("Guess Number Game 🥸 \nMy eyes are on your mind 🫵.")

    @staticmethod
    def prompt_user_input() -> int: 
        while True:
            try:
                user_input = int(input(">> "))
                return user_input
            except ValueError:
                return 0

class GuessingGame(Game):
    ui: TerminalUI

    def __init__(self) -> None:
        self.ui = TerminalUI()
    
    def run(self, player:int) -> None:
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

        results = session.calculate_score(str(user_input))
        self.coins = int(results["coins"])
        save_score(player, 1, session._get_elapsed_time(), self.coins)
        self.ui.display_score_card(results)

    def get_coins(self) -> float:
        return self.coins
