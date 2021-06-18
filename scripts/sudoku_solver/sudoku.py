class Cell:
    def __init__(self, value=None):
        self.value = value
        self.possibilities = None if value else set(range(1,10))

    def __repr__(self):
        if self.value:
            return f'Cell: {self.value}'
        else:
            return f'Cell: {self.possibilities}'

    def remove(self, number):
        self.values.remove(number)


class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = self._create_sudoku(sudoku)

    def __repr__(self):
        return f''

    def _create_sudoku(self, sudoku):
        for i, row in enumerate(sudoku):
            for j, val in enumerate(row):
                if val != 0:
                    sudoku[i][j] = Cell(val)
                else:
                    sudoku[i][j] = Cell()

        return sudoku

    def cols(self):
        row = 0
        col = 0
        while col < 9:
            while row < 9:
                yield self.sudoku[col][row]
                row += 1

            row = 0
            col += 1

    def rows(self):
        row = 0
        col = 0
        while row < 9:
            while col < 9:
                yield self.sudoku[col][row]
                col += 1

            col = 0
            row += 1

    def boxes():
        centers = [()]
