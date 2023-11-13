# controllers.py

import logging
from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from services import fetch_top_players, fetch_player_rating_history
from models import PlayerRatingHistory
from database import SessionLocal
import csv
from io import StringIO

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_rating_history_to_db(db: Session, username, rating_history_data):
    # Save to the database
    db_player = PlayerRatingHistory(username=username, rating_history=rating_history_data)
    db.add(db_player)
    db.commit()

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/top-players")
async def get_top_players():
    top_players_data = await fetch_top_players()
    return {"top_players": top_players_data[:50]}

@app.get("/player/{username}/rating-history")
async def get_player_rating_history(username: str, db: Session = Depends(get_db)):
    rating_history_data = await fetch_player_rating_history(username)
    save_rating_history_to_db(db, username, rating_history_data)
    return {"rating_history": rating_history_data}

@app.get("/players/rating-history-csv")
async def get_rating_history_csv(db: Session = Depends(get_db)):
    top_players_data = await fetch_top_players()

    # Prepare CSV data
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerow(["Username", "Rating 30 Days Ago", "Rating on Each Subsequent Day"])

    for player in top_players_data[:50]:
        if isinstance(player, dict) and "username" in player:
            player_username = player["username"]
            rating_history_data = await fetch_player_rating_history(player_username)
            save_rating_history_to_db(db, player_username, rating_history_data)

            # Extract relevant data for CSV
            username = player_username
            rating_30_days_ago = rating_history_data[0]["rating"] if rating_history_data else "N/A"
            rating_history = [entry["rating"] for entry in rating_history_data]

            csv_writer.writerow([username, rating_30_days_ago] + rating_history)

    # Return CSV as a response
    response = Response(content=csv_data.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"
    return response
