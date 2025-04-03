from . import db
from datetime import datetime
from sqlalchemy import Sequence


class Products(db.Model):
    __bind_key__ = 'db'
    id = db.Column(db.Integer, Sequence('Products_sequence'), unique=True, nullable=False, primary_key=True)
    products_id = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    medicine_type_id = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    requires_prescription = db.Column(db.String(255), nullable=False)
    created_by = db.Column(db.TIMESTAMP, default=datetime.now)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
