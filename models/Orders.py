from . import db
from datetime import datetime
from sqlalchemy import Sequence

class Orders(db.Model):
    __bind_key__ = 'db'
    id = db.Column(db.Integer, Sequence('Products_sequence'), unique=True, nullable=False, primary_key=True)
    user_id = db.Column(db.String(255),nullable=False)
    order_date = db.Column(db.TIMESTAMP, default=datetime.now)
    total_amount = db.Column(db.Float)
    status = db.Column(db.String(50))


