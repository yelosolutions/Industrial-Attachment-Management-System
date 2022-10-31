from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    requests = db.relationship('Request', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    contact = db.Column(db.String(128))
    period = db.Column(db.Date())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Request {}>'.format(self.request_id)