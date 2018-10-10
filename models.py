# coding=utf-8
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    message = db.relationship("Message")

    def __repr__(self):
        return '<User {}>'.format(self.username)  

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direction = db.Column(db.String(64))
    message = db.Column(db.String(2500))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    def __repr__(self):
        return '<Message {}>'.format(self.message)  
