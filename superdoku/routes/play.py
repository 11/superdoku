import json

from http import HTTPStatus as status

from flask import (
    Blueprint,
    Response,
    render_template,
)

from models.sudoku import Sudoku


bp = Blueprint('play_route', __name__, url_prefix='/play')


@bp.route('/<id>', methods=['GET'])
def render_play(id):
    sudoku = Sudoku.query.filter_by(id=id).first()
    if (not sudoku):
        resp = { 'message': 'could not find puzzle' }
        return Response(
            json.dumps(resp),
            status=status.NOT_FOUND,
            mimetype='application/json'
        )

    return render_template('play.jinja', puzzle=sudoku.puzzle)
