from fastapi import FastAPI
from app.db.database import get_connection

app = FastAPI(title="FootIQ API")


@app.get("/")
def root():
    return {"message": "Welcome to FootIQ API"}


@app.get("/teams")
def get_teams():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, country, league
                FROM teams
                ORDER BY name;
            """)

            teams = cursor.fetchall()

            return [
                {
                    "id": team[0],
                    "name": team[1],
                    "country": team[2],
                    "league": team[3]
                }
                for team in teams
            ]

    finally:
        connection.close()


@app.get("/players")
def get_players():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    players.id,
                    players.name,
                    players.age,
                    players.position,
                    players.nationality,
                    teams.name AS team
                FROM players
                JOIN teams ON players.team_id = teams.id
                ORDER BY players.name;
            """)

            players = cursor.fetchall()

            return [
                {
                    "id": player[0],
                    "name": player[1],
                    "age": player[2],
                    "position": player[3],
                    "nationality": player[4],
                    "team": player[5]
                }
                for player in players
            ]

    finally:
        connection.close()


@app.get("/players/{player_id}")
def get_player(player_id: int):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    players.id,
                    players.name,
                    players.age,
                    players.position,
                    players.nationality,
                    teams.name AS team
                FROM players
                JOIN teams ON players.team_id = teams.id
                WHERE players.id = %s;
            """, (player_id,))

            player = cursor.fetchone()

            if player is None:
                return {"error": "Player not found"}

            return {
                "id": player[0],
                "name": player[1],
                "age": player[2],
                "position": player[3],
                "nationality": player[4],
                "team": player[5]
            }

    finally:
        connection.close()