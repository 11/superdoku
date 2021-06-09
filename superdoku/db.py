import os

from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

def create_db():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_HOST')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy()
    return db
