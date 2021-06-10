from datetime import datetime
from extensions import db


class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(120), primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    salt = db.Column(db.String(32), unique=True, nullable=False)
    hash = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, first_name, last_name, salt, hash):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.salt = salt
        self.hash = hash

    def __repr__(self):
        return f'email: {self.email}\nfirst: {self.first_name}\nlast: {self.last_name}\ncreated_at:{self.created_at}'
