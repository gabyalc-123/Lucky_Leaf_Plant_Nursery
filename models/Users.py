from . import db
from datetime import datetime
from sqlalchemy import Sequence

# table
class Users(db.Model):
    __bind_key__ = 'db'

    #primary key id
    id = db.Column(db.Integer, Sequence('users_sequence'), unique=True, nullable=False, primary_key=True)
    user_id = db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)