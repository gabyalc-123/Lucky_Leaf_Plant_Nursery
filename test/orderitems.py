from . import db
from datetime import datetime
from sqlalchemy import Sequence


class OrderItems(db.Model):
    id = db.Column(db.Integer, Sequence('Products_sequence'), unique=True, nullable=False, primary_key=True)
    order_items_id = db.Column(db.String(255), nullable=False)
    orders_id = db.Column(db.String(255), nullable=False)
    products_id = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
