from . import db
from datetime import datetime
from sqlalchemy import Sequence

class Products(db.Model):
    __bind_key__ = 'db'
    id = db.Column(db.Integer, Sequence('users_sequence'), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    plant_type_id = db.Column(db.String(255))
    stock = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    created_by = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)

