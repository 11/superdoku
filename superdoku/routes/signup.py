import json

from flask import Blueprint, render_template, request, Response

from extensions import db
from common import password as pwd_helper
from models.user import User


bp = Blueprint('signup_blueprint', __name__, url_prefix='/signup')


@bp.route('/')
def signup_page():
    return render_template('signup.jinja')


@bp.route('/', methods=['POST'])
def signup():
    first = request.form.get('firstname')
    last = request.form.get('lastname')
    email = request.form.get('email')
    pwd = request.form.get('password')
    if (not (first and last and email and pwd)):
        resp = { 'message': 'must submit all forms values' }
        return Response(json.dumps(resp), status=400, mimetype='application/json')

    salt, hash = pwd_helper.encrypt(pwd)
    user = User(email, first, last, salt, hash)
    db.session.add(user)
    db.session.commit()

    resp = { 'message': 'success' }
    return Response(json.dumps(resp), status=201, mimetype='application/json')
