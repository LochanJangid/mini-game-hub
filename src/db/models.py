from db.connection import get_db


def register_player(name: str):
    db = get_db()
    db.query("INSERT INTO players (name) VALUES (?)", (name, ))
    row = db.query("SELECT last_insert_rowid()", operation="fetchone")
    return row[0]

def save_score(player_id: int, game_id: int, duration: int, earned_coins: int):
    db = get_db()
    db.query("INSERT INTO sessions (player_id, game_id, duration, earned_coins) VALUES (?, ?, ?, ?)", (player_id, game_id, duration, earned_coins))