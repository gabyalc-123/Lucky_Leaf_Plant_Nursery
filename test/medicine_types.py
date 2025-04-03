from . import db
from datetime import datetime
from sqlalchemy import Sequence


class MedicineTypes(db.Model):
    __bind_key__ = 'db'
    id = db.Column(db.Integer, Sequence('MedicineTypes_sequence'), unique=True, nullable=False, primary_key=True)
    medicine_types_id = db.Column(db.String(255), nullable=False)

    type_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)


    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
