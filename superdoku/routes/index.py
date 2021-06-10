from flask import Blueprint
from flask.templating import render_template


bp = Blueprint('index_blueprint', __name__, url_prefix='/')


@bp.route('/')
def homepage():
    return render_template('index.jinja')
