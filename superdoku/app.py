from flask import Flask

from extensions import db
from routes.index import index_blueprint as index_route
from routes.login import login_blueprint as login_route
from routes.signup import signup_blueprint as signup_route


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(index_route)
    app.register_blueprint(login_route)
    app.register_blueprint(signup_route)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('localhost', port=7000, debug=True)
