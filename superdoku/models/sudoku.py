from extensions import db

class Sudoku(db.Column):
    __tablename__ = 'sudoku'

    puzzle = db.Column(db.String(81), unique=True, nullable=False)

