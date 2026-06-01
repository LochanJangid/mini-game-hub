from src.db.connection import get_db
from typing import Dict

def login_player(name: str):
    db = get_db()
    row = db.query("SELECT id FROM players WHERE name = ?", (name, ), operation="fetchone")
    if not row:
        db.query("INSERT INTO players (name) VALUES (?)", (name, ))
        row = db.query("SELECT last_insert_rowid()", operation="fetchone")
    return row[0]

def save_score(player_id: int, game_id: int, duration: float, earned_coins: int):
    db = get_db()
    db.query("INSERT INTO sessions (player_id, game_id, duration, earned_coins) VALUES (?, ?, ?, ?)", (player_id, game_id, duration, earned_coins))

def insert_games(games: Dict[int, str]):
    db = get_db()
    for k, v in games.items():
        db.query("""
        INSERT INTO games (id, name)
        VALUES (?, ?)
        ON CONFLICT(id) DO NOTHING;
            """, (k, v))

def get_leaderboard():
    db = get_db()
    rows = db.query("""
        SELECT *, 
               DENSE_RANK() OVER(ORDER BY coins DESC) AS coin_rank 
          FROM (
            SELECT players.name, 
                   SUM(earned_coins) AS coins
            FROM sessions 
            JOIN players ON sessions.player_id=players.id
            GROUP BY players.id, players.name 
        ) AS tb;
        """, operation="fetchall")
    return rows
    