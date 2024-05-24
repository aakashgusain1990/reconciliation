from app import db
from datetime import datetime

class Customer(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    phone_no: str = db.Column(db.String(100))
    email: str = db.Column(db.String(100))
    link_id: int = db.Column(db.Integer)
    link_tye: str = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow) 
    deleted_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f'<Customer {self.phone_no} {self.email}>'
    