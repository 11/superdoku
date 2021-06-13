from extensions import db


class Sudoku(db.Model):
    __tablename__ = 'sudoku'

    id = db.Column(db.Integer, primary_key=True)
    puzzle = db.Column(db.String(81), unique=True, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, puzzle, difficulty):
       self.puzzle = puzzle
       self.difficulty = difficulty

    def __repr__(self):
        return f'id: {self.id}\npuzzle: {self.puzzle}\ndifficulty: {self.difficulty}'
