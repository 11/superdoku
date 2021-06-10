from flask import Blueprint

from ..extensions import db
from ..models import Sudoku


sudoku_route = Blueprint('sudoku_route', __name__)

@sudoku_route.route('/puzzle', methods=['POST'])
def create():
    sudoku = Sudoku('')