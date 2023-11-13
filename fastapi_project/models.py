# models.py

from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PlayerRatingHistory(Base):
    __tablename__ = "player_rating_history"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    rating_history = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
