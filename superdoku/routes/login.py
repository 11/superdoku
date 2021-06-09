from flask import Blueprint, render_template

login_blueprint = Blueprint('login_blueprint',  __name__)

@login_blueprint.route('/login', methods=['GET'])
def render():
    return render_template('login.html')


@login_blueprint.route('/login', methods=['POST'])
def sign_in():
    pass
