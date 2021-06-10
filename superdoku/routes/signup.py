import json

from http import HTTPStatus as status

from flask import (
    Blueprint,
    Response,
    render_template,
    request as req,
)

from common import password as pwd_helper
from extensions import db
from models.user import User


bp = Blueprint('signup_blueprint', __name__, url_prefix='/signup')


@bp.route('/')
def signup_page():
    return render_template('signup.jinja')


@bp.route('/', methods=['POST'])
def signup():
    first = req.form.get('firstname')
    last = req.form.get('lastname')
    email = req.form.get('email')
    pwd = req.form.get('password')

    if (not (first and last and email and pwd)):
        resp = { 'message': 'must submit all forms values' }
        return Response(
            json.dumps(resp),
            status=status.BAD_REQUEST,
            mimetype='application/json'
        )

    salt, hash = pwd_helper.encrypt(pwd)
    user = User(email, first, last, salt, hash)
    db.session.add(user)
    db.session.commit()

    resp = { 'message': 'success' }
    return Response(
        json.dumps(resp),
        status=status.CREATED,
        mimetype='application/json'
    )
