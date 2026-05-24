from db.connection import get_db


def login_player(name: str):
    db = get_db()
    row = db.query("SELECT id FROM players WHERE name = ?", (name, ), operation="fetchone")
    if not row:
        db.query("INSERT INTO players (name) VALUES (?)", (name, ))
        row = db.query("SELECT last_insert_rowid()", operation="fetchone")
    return row[0]

def save_score(player_id: int, game_id: int, duration: int, earned_coins: int):
    db = get_db()
    db.query("INSERT INTO sessions (player_id, game_id, duration, earned_coins) VALUES (?, ?, ?, ?)", (player_id, game_id, duration, earned_coins))

def get_leaderboard():
    db = get_db()
    rows = db.query("""
        SELECT players.name, SUM(earned_coins) AS coins
          FROM sessions 
          JOIN players ON player_id=players.id
        GROUP BY player_id 
        ORDER BY coins
        LIMIT 3;""", operation="fetchall")
    return rows
    