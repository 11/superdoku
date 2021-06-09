from flask import Blueprint
from flask.templating import render_template


index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/')
def homepage():
    return render_template('index.jinja')
