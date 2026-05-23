from sqliter import Database

DB_PATH = "game.db"

class GameDb:
    """Handles the database connection for the game."""
    def __init__(self):
        self.db = Database(DB_PATH)

    def get_db(self):
        return self.db