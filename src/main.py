import sys

from src.db.models import login_player
from src.first_run import execute_setup
from src.games.guessing_game import GuessingGame
from src.games.tic_tac_toe import ToeGame
from src.games.typing_game import TypingGame
from src.ui.main_ui import MainUI

MAP = {
    "Typing Speed Test": TypingGame,
    "Guess Number Game": GuessingGame,
    "Tic Tac Toe": ToeGame,
}

GAMES = {0: "Typing Speed Test", 1: "Guess Number Game", 2: "Tic Tac Toe"}


def main():
    execute_setup(GAMES)
    ui = MainUI()
    ui.intro("👾 Mini Game Hub 🎮", "Your central hub for Python mini-games 🎮.")
    ui.show_leaderboard()
    player = login_player(ui.prompt_player_name())
    print("Welcome", player)
    ui.show_commands(GAMES)
    while True:
        try:
            user_command = int(ui.prompt_command())
            game = MAP[GAMES[user_command]]()
            game.run(player)
            break
        except (KeyError, ValueError):
            print("❌ Invalid command! Commands are:")
            ui.show_commands(GAMES)
        except KeyboardInterrupt:
            ui.bye()
            sys.exit(0)


if __name__ == "__main__":
    main()
