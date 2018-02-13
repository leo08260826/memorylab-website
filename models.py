from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, default='')
    questions = db.relationship(
        'Question',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), default='')
    picture_url = db.Column(db.String(80), default='')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, description='', picture_url=''):
        self.description = description
        self.picture_url = picture_url

    def __repr__(self):
        return '<Question %r %r>' % ( self.description, self.picture_url)
