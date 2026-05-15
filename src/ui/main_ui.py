import time
from src.ui.components import title

class MainUI:

    def intro(self, name: str, tagline: str) -> None:
        for ch in name:
            print(ch, end='', flush=True)
            time.sleep(0.10)
        print()
        for word in tagline:
            print(word, end='', flush=True)
            time.sleep(0.005)
        print()

    def show_commands(self, games: dict) -> None:
        for i, game in zip(range(0, len(games)), games):
            print(f"{i}: {game}")
            time.sleep(0.005)
    
    def prompt_command(self) -> str:
        return input("Enter a command: ")
    
    def bye(self) -> None:
        print()
        title("Bye, See you tommorow :)", "Stay Hydrated. 🍼")
            

        

        


