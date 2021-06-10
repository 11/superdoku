import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))

PEPPER=os.environ.get('PEPPER')
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_HOST')
SQLALCHEMY_TRACK_MODIFICATIONS = False
