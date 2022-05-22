# from typing_extensions import Self
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
# define a champion class that inherits from db.Model
class Champion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    role = db.Column(db.String(64))
    year = db.Column(db.Integer)
    skins = db.Column(db.Integer)

    
    def __repr__(self):
        return '<Champion {}>'.format(self.name)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    scores = db.relationship('Score', backref='summoner', lazy='select', uselist=False) #Link User and Score Database
    # Unsure what backref=taker means

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Datbase fields to be updated
    onlineGamesPlayed = db.Column(db.Integer)
    onlineGamesWon = db.Column(db.Integer)
    onlineAverageGuesses = db.Column(db.Integer)
    # Links score database to user db 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Score {}>'.format(self.onlineGamesWon) 
        # The above line may need to be changed 


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


