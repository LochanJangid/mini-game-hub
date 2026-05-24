from src.games.base_game import GameUI, Game, GameSession
from src.ui.components import box

class TerminalSession(GameSession):
    board: list[list[int]]

    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

class TerminalUI(GameUI):
    
    @staticmethod
    def display_title() -> None:
        """Displays the title of the game."""
        box("Tic Tac Toe 🐒 \nplay tici taca taca")

    def show_board(self, board: list[list[int]]) -> None:
        """Display updated board."""
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()
        


class ToeGame(Game):
    ui: TerminalUI

    def __init__(self):
        self.ui = TerminalUI()

    def run(self, player:int) -> None:
        """Center point of the game."""
        self.ui.display_title()

    def get_coins(self) -> float:
        return 0.0    