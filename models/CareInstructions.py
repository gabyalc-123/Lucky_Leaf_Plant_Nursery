from . import db
from datetime import datetime
from sqlalchemy import Sequence

class CareInstructions(db.Model):
    __bind_key__ = 'db'
    id = db.Column(db.Integer, Sequence('Products_sequence'), unique=True, nullable=False, primary_key=True)
    product_id = db.Column(db.String(255),nullable=False)
    instructions = db.Column(db.String(500), nullable=False)
