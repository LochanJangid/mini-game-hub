import time
from src.ui.components import box
from src.db.models import get_leaderboard

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

    def prompt_player_name(self) -> str:
        player = input(":: What is Your Name: ")
        return player
        
    def show_commands(self, games: dict) -> None:
        for k, game in games.items():
            print(f"{k}: {game}")
            time.sleep(0.005)
    
    def prompt_command(self) -> str:
        return input("Enter a command: ")

    def show_leaderboard(self):
        leaders = get_leaderboard()
        if not leaders:
            print("╭────────────────────────╮")
            print("│ No scores yet!         │")
            print("╰────────────────────────╯")
            return

        max_name = max((len(str(d["name"])) for d in leaders), default=6)
        name_w = max(max_name, 10)
        rank_w = 4
        score_w = 8
        total_w = rank_w + name_w + score_w + 8
        
        print(f"╭{'─' * total_w}╮")
        print(f"│{"🐒 LEADERBOARD 🐒".center(total_w)}│")
        print(f"├{'─' * (rank_w + 2)}┬{'─' * (name_w + 2)}┬{'─' * (score_w + 2)}┤")
        print(f"│ {'Rank':<{rank_w}} │ {'Name':<{name_w}} │ {'Coins':>{score_w}} │")
        print(f"├{'─' * (rank_w + 2)}┼{'─' * (name_w + 2)}┼{'─' * (score_w + 2)}┤")

        for leader in leaders:
            print(f"│ {leader["rank"]:<{rank_w}} │ {leader["name"]:<{name_w}} │ {leader["coins"]:>{score_w}} │")

        print(f"╰{'─' * (rank_w + 2)}┴{'─' * (name_w + 2)}┴{'─' * (score_w + 2)}╯")

        
    def bye(self) -> None:
        print()
        box("Bye, See you tommorow :) \nStay Hydrated. 🍼")
    

        

        


