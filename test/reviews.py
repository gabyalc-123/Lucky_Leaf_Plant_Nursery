from . import db
from datetime import datetime
from sqlalchemy import Sequence


class Reviews(db.Model):
    id = db.Column(db.Integer, Sequence('Products_sequence'), unique=True, nullable=False, primary_key=True)
    order_items_id = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    products_id = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    review_date = db.Column(db.TIMESTAMP, default=datetime.now)
