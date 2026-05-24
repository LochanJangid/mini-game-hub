from src.db.create_tables import create_tables
from src.db.models import insert_games
from typing import Dict


def execute_setup(games: Dict[int, str]):
    create_tables()
    insert_games(games)
        