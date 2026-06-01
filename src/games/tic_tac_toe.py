import time
import random
from typing import Dict, Union, List
from src.ui.components import box
from src.games.base_game import Game, GameSession, GameUI
from src.db.models import save_score

class ToeSession(GameSession):
    """Handles the board state, game logic, and score calculation for Tic Tac Toe."""
    def __init__(self) -> None:
        self.board: List[str] = [str(i) for i in range(1, 10)]
        self.moves_made: int = 0
        self.winner: Union[str, None] = None
        self.winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

    def get_available_moves(self) -> List[int]:
        """Returns a list of available board indices."""
        return [i for i, cell in enumerate(self.board) if cell not in ('X', 'O')]

    def place_marker(self, index: int, marker: str) -> bool:
        """Places a marker on the board. Returns True if successful."""
        if index in self.get_available_moves():
            self.board[index] = marker
            self.moves_made += 1
            self.check_winner()
            return True
        return False

    def check_winner(self) -> None:
        """Evaluates the board to see if there is a winner."""
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                self.winner = self.board[combo[0]]
                return

    def get_computer_move(self) -> int:
        """Determines the computer's ('O') next move using basic logic."""
        available = self.get_available_moves()
        
        # 1. computer try to win if possible :)
        for move in available:
            self.board[move] = 'O'
            if self._sim_check_winner() == 'O':
                self.board[move] = str(move + 1)
                return move
            self.board[move] = str(move + 1)

        # 2. try to block player if he will win in next move
        for move in available:
            self.board[move] = 'X'
            if self._sim_check_winner() == 'X':
                self.board[move] = str(move + 1)
                return move
            self.board[move] = str(move + 1)

        # 3. Take center if available
        if 4 in available:
            return 4

        # 4. Pick randomly because computer don't have its own mind :(
        return random.choice(available)

    def _sim_check_winner(self) -> Union[str, None]:
        """Helper for computer to check win states without mutating main game state."""
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return self.board[combo[0]]
        return None

    def calculate_score(self, user_input: str = "") -> Dict[str, Union[int, float, str]]:
        """Calculates results based on the game's outcome."""
        elapsed = round(self._get_elapsed_time(), 2)

        if self.winner == 'X':
            outcome = "Victory"
            coins = max(10, 50 - int(elapsed)) # Faster wins yield more coins
        elif self.winner == 'O':
            outcome = "Defeat"
            coins = 0
        else:
            outcome = "Draw"
            coins = 5

        return {
            "outcome": outcome,
            "moves": self.moves_made,
            "coins": coins
        }


class TerminalUI(GameUI):
    """Handles all terminal inputs, outputs, and formatting for the game."""

    @staticmethod
    def display_title() -> None:
        """Displays the game title."""
        box("Tic Tac Toe vs CPU 🤖 \nMan vs Machine!")

    @staticmethod
    def show_board(board: List[str]) -> None:
        """Displays the updated 3x3 board."""
        print("\n")
        print(f" {board[0]} │ {board[1]} │ {board[2]} ")
        print("───┼───┼───")
        print(f" {board[3]} │ {board[4]} │ {board[5]} ")
        print("───┼───┼───")
        print(f" {board[6]} │ {board[7]} │ {board[8]} ")
        print("\n")

    @staticmethod
    def prompt_move(available_moves: List[int]) -> int:
        """Prompts the user for a move and handles input errors."""
        available_display = [m + 1 for m in available_moves]
        while True:
            try:
                user_input = int(input(f"Your move 'X' {available_display}: >> "))
                index = user_input - 1
                if index in available_moves:
                    return index
                print("❌ Cell already taken or invalid. Choose an available number.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")


class ToeGame(Game):
    """The main controller coordinating the Tic Tac Toe flow."""
    ui: TerminalUI
    coins: int

    def __init__(self) -> None:
        self.ui = TerminalUI()
        self.coins = 0

    def run(self, player: int) -> None:
        """The center point which connects everything and runs the game."""
        self.ui.display_title()
        session = ToeSession()
        
        print("When you're ready, hit enter ↲ to start.")
        input()  # Start Trigger
        
        session.start()
        
        while not session.winner and session.moves_made < 9:
            self.ui.show_board(session.board)
            
            # Player's Turn
            player_move = self.ui.prompt_move(session.get_available_moves())
            session.place_marker(player_move, 'X')
            
            if session.winner or session.moves_made == 9:
                break
                
            # Computer's Turn
            print("\nComputer 'O' is thinking...")
            time.sleep(0.5) # Artificial delay for pacing
            comp_move = session.get_computer_move()
            session.place_marker(comp_move, 'O')

        session.stop()
        self.ui.show_board(session.board)
        
        # Calculate and Display Results
        results = session.calculate_score()
        self.coins = int(results["coins"])
        
        # Save score assuming the same DB structure from the TypingGame
        try:
            save_score(player, 0, session._get_elapsed_time(), self.coins)
        except NameError:
            pass # Fallback if save_score isn't imported
            
        self.ui.display_score_card(results)

    def get_coins(self) -> float:
        return float(self.coins)