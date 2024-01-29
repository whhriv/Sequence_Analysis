import os
from app import db, login
import base64
from datetime import datetime, timedelta
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password', ''))

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)
    
    def __repr__(self):
        return f"<Username {self.id}, Username={self.id}>"
    
    def get_id(self):
        return self.id  
    

@login.user_loader
def get_user(user_id):
    return db.session.get(User, user_id)
    
class SequenceForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    isolate =  db.Column(db.String, nullable=False)
    gene =  db.Column(db.String, nullable=False)
    location =  db.Column(db.String, nullable=False)
    lat =  db.Column(db.String, nullable=False)
    long =  db.Column(db.String, nullable=False)
    assension =  db.Column(db.String, nullable=False)
    sequenceRAW =  db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<SEQUENCE {self.id}|{self.username}>"

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'isolate': self.isolate,
            'gene': self.gene,
            'location': self.location,
            'latitude': self.lat,
            'longitude': self.long,
            'assension': self.assension,
            'Date' : self.date_created,
            'Sequence' : self.sequence

        }
        
