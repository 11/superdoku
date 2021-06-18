def _filter_rows(sudoku):
    for row in sudoku.rows():
        possible_values = set(range(1,10))

        for cell in row:
            if cell.num != 0:
                possible_values.remove(cell.num)

        for cell in row:
            if cell.num == 0:
                cell.values -= possible_values


def _filter_columns(sudoku):
    for col in sudoku.cols():
        possible_values = set(range(1,10))
        for cell in col:
            if cell.num != 0:
                possible_values.remove(cell.num)

        for cell in col:
            if cell.num == 0:
                cell.values -= possible_values



def _filter_boxes(sudoku):
    for box in sudoku.boxes():
        possible_values = set(range(1,10))
        for cell in box:
            if cell.num != 0:
                possible_values.remove(cell.num)

        for cell in box:
            if cell.num == 0:
                cell.values -= possible_values


def _fill_cells(sudoku):
    for row in sudoku.sudoku:
        for cell in row:
            cell.fill()


def solve(sudoku):
    while True:
        # backtrace through grid and update cells with any possible values
        _filter_rows(sudoku)
        _filter_columns(sudoku)
        _filter_boxes(sudoku)

        # update all cells that only have 1 possibility left
        # break out if sudoku is solved or their is no solution
        if sudoku.is_solved():
            break
        elif not sudoku.is_updateable():
            raise ValueError('ERROR - Sudoku is unsolvable')
        else:
            _fill_cells(sudoku)

    print(sudoku) # print solution in sudoku grid style
    # sudoku.print_flat() # print db string
