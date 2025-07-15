from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    initial_velocity = db.Column(db.Float, nullable=False)
    angle = db.Column(db.Float, nullable=False)
    trajectory = db.Column(db.JSON, nullable=False)
    user = db.relationship('User', backref=db.backref('calculations', lazy=True))