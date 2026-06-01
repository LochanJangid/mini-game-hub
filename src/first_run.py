from src.db.create_tables import create_tables
from src.db.models import insert_games
from typing import Dict

def execute_setup(games: Dict[int, str]):
    local_games = games.copy()
    create_tables()
    local_games.pop(9, None)
    insert_games(local_games)