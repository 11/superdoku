from flask import Blueprint, render_template

bp = Blueprint('login_blueprint',  __name__, url_prefix='/login')


@bp.route('/', methods=['GET'])
def render():
    return render_template('login.jinja')


@bp.route('/', methods=['POST'])
def sign_in():
    pass
