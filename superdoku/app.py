from flask import Flask

from extensions import db, migrate

from models import *

from routes.index import bp as index_bp
from routes.login import bp as login_bp
from routes.signup import bp as signup_bp
from routes.sudoku import bp as sudoku_bp
from routes.play import bp as play_bp


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(sudoku_bp)
    app.register_blueprint(play_bp)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app)

        db.create_all()
        db.session.commit()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('localhost', port=7000, debug=True)
