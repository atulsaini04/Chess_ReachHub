# services.py

import httpx

async def fetch_top_players():
    lichess_api_token = "your_token"
    top_players_url = "https://lichess.org/api/player/top/500/classical"

    async with httpx.AsyncClient() as client:
        top_players_response = await client.get(top_players_url)
        top_players_data = top_players_response.json()

    return top_players_data

async def fetch_player_rating_history(username):
    lichess_api_token = "your_token"
    rating_history_url = f"https://lichess.org/api/user/{username}/rating-history"

    async with httpx.AsyncClient() as client:
        rating_history_response = await client.get(rating_history_url)
        rating_history_data = rating_history_response.json()

    return rating_history_data
