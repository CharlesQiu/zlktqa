# encoding: utf-8

from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Question(db.Model):
    __tablename__ = 'question'
    qid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    author = db.relationship('User', backref=db.backref('questions'))


class Comment(db.Model):
    __tablename__ = 'comment'
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    qid = db.Column(db.Integer, db.ForeignKey('question.qid'))
    aid = db.Column(db.Integer, db.ForeignKey('user.uid'))

    question = db.relationship('Question', backref=db.backref('comments', order_by=create_time.desc()))
    author = db.relationship('User', backref=db.backref('comments'))
