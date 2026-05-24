from sqliter import Database

DB_PATH = "game.db"

def get_db():
    return Database(DB_PATH)