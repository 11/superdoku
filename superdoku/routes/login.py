import json
from http import HTTPStatus as status

from flask import (
    Response,
    Blueprint,
    render_template,
    request as req,
)

from common import password as pwd_helper
from models.user import User


bp = Blueprint('login_blueprint',  __name__, url_prefix='/login')


@bp.route('/', methods=['GET'])
def login_page():
    return render_template('login.jinja')


@bp.route('/', methods=['POST'])
def login():
    email = req.form.get('email')
    pwd = req.form.get('password')

    user = User.query.filter_by(email=email).first()
    if (not user):
        resp = { 'message': f'can\'t find user with email `{email}`' }
        return Response(
            json.dumps(resp),
            status=status.NOT_FOUND,
            mimetype='application/json'
        )

    hash = pwd_helper.decrypt(pwd, user.salt)
    if hash != user.hash:
        resp = { 'message': 'password was incorrect' }
        return Response(
            json.dumps(resp),
            status=status.BAD_REQUEST,
            mimetype='application/json'
        )

    resp = { 'message': 'password was incorrect' }
    return Response(
        json.dumps(resp),
        status=status.OK,
        mimetype='application/json'
    )
