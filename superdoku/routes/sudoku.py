import json

from http import HTTPStatus as status

from extensions import db
from models.sudoku import Sudoku

from flask import (
    Blueprint,
    Response,
    render_template,
    request as req
)

bp = Blueprint('sudoku_route', __name__, url_prefix='/sudoku')


@bp.route('/', methods=['GET'])
def render_sudoku():
    return render_template('create_sudoku.jinja')


@bp.route('/', methods=['POST'])
def add_sudoku():
    puzzle_str = req.form.get('puzzle')
    difficulty = req.form.get('difficulty')

    sudoku = Sudoku(puzzle=puzzle_str, difficulty=difficulty)
    if not sudoku:
        err_json = { 'message': 'failed to create sudoku' }
        return Response(
            json.dumps(err_json),
            status=status.BAD_REQUEST,
            mimetype='application/json')

    db.session.add(sudoku)
    db.session.commit()

    success_json = { 'message': 'successfully added a new sudoku to the DB' }
    return Response(
        json.dumps(success_json),
        status=status.CREATED,
        mimetype='application/json')
