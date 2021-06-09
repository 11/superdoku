from flask import Flask
from dotenv import find_dotenv, load_dotenv

from db import create_db

from routes.index import index_blueprint as index_route
from routes.login import login_blueprint as login_route
from routes.signup import signup_blueprint as signup_route


load_dotenv(find_dotenv('.env'))

app = Flask(__name__)
app.register_blueprint(index_route)
app.register_blueprint(login_route)
app.register_blueprint(signup_route)


if __name__ == '__main__':
    with app.app_context():
        db = create_db()
        db.init_app(app)
        db.create_all()

    app.run('localhost', port=7000, debug=True)
