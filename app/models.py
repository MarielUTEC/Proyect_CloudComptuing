from enum import unique

from sqlalchemy import PrimaryKeyConstraint
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    points = db.Column(db.String(64), index=True)
   

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    url = db.Column(db.String(120), index = True, unique = True)



class VideoMusic(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    url = db.Column(db.String(250), index = True, unique = True)
    title = db.Column(db.String(120), index = True)
    banner= db.Column(db.String(250), index = True )
    views = db.Column(db.Integer, index = True)


class Detalle_Score(db.Model): 
    TimeSeg = db.Column(db.Integer, priamry_key = True, unique = True)
    Correct = db.Column(db.Integer, integer = True)
    Incorrect = db.Column(db.Integer, integer = True)


db.create_all()


