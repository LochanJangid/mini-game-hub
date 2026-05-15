import sys
from src.games.typing_game import TypingGame
from src.games.guessing_game import GuessingGame
from src.ui.main_ui import MainUI

GAMES = {
    'Typing Speed Test': TypingGame,
    'Guess Number Game': GuessingGame
}

COMMAND_MAP = {
    0: 'Typing Speed Test',
    1: 'Guess Number Game'
}

def main():
    ui = MainUI()
    ui.intro('👾 Mini Game Hub 🎮', 'Your central hub for Python mini-games 🎮.')
    ui.show_commands(GAMES)
    while True:
        try:
            user_command = int(ui.prompt_command())
            game = GAMES[COMMAND_MAP[user_command]]()
            game.run()
            break
        except (KeyError, ValueError):
            print("❌ Invalid command! Commands are:")
            ui.show_commands(GAMES)
        except KeyboardInterrupt:
            ui.bye()
            sys.exit(0)

if __name__ == "__main__":
    main()
