from app import db
from dataclasses import dataclass


@dataclass
class Team(db.Model):
    
    __tablename__ = 'teams'
    id =db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name', db.String(255))
    sport = db.Column('sport', db.String(255))
    league = db.Column('league', db.String(255))