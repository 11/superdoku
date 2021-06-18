from collections import namedtuple


class Cell:
    def __init__(self, num=0):
        self._num = num
        self._values = set(range(1,10)) if num == 0 else None

    def __repr__(self):
        return str(self.num)

    def is_fillable(self):
        return len(self._values) == 1 and self._num == 0

    def fill(self):
        if len(self._values) == 1 and self._num == 0:
            num = self._values.pop()
            self._num = num

    @property
    def num(self):
        return self._num

    @property
    def values(self):
        return self._values

    @property.setter
    def values(self, val):
        self._values = val


class Sudoku:
    def __init__(self, sudoku):
        self._sudoku = self._create_sudoku(sudoku)

    def __repr__(self):
        sudoku_str = ''
        for row in self._sudoku:
            for num in row:
                sudoku_str += f'{num} '

            sudoku_str += '\n\n'

        return sudoku_str

    def print_flat(self):
        pass

    @property
    def sudoku(self):
        return self._sudoku

    def _create_sudoku(self, sudoku):
        for i, row in enumerate(sudoku):
            for j, val in enumerate(row):
                sudoku[i][j] = Cell(val)

        return sudoku

    def is_updateable(self):
        for row in self._sudoku:
            for cell in row:
                if cell.is_fillable():
                    return True

        return False

    def is_solved(self):
        for row in self._sudoku:
            for cell in row:
                if cell.num == 0:
                    return False

        return True

    def rows(self):
        for row in self._sudoku:
            yield row

    def cols(self):
        row = 0
        col = 0
        while col < 9:
            curr_col = []
            while row < 9:
                curr_col.append(self._sudoku[row][col])
                row += 1

            yield curr_col
            row = 0
            col += 1

    def boxes(self):
        Center = namedtuple('Center', ['x', 'y'])
        center_coordinates = [
            Center(1, 1), # top left
            Center(1, 4), # top mid
            Center(1, 7), # top right
            Center(4, 1), # mid left
            Center(4, 4), # mid mid
            Center(4, 7), # mid right
            Center(7, 1), # bottom left
            Center(7, 4), # bottom mid
            Center(7, 7), # bottom right
        ]

        box_cells = lambda x, y: [
            (x - 1, y - 1), # top left
            (x - 1, y),     # top mid
            (x - 1, y + 1), # top right
            (x, y - 1),     # mid left
            (x, y),         # mid mid
            (x, y + 1),     # mid right
            (x + 1, y - 1), # bottom left
            (x + 1, y),     # bottom mid
            (x + 1, y + 1), # bottom right
        ]

        for center in center_coordinates:
            box = box_cells(center.x, center.y)
            yield box
