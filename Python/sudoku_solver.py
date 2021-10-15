import numpy as np
initial_grid = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0 , 0 ,4 ,0 ,0 ,0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]



def check_dupicate(grid, row, column, n):
    for i in range(9):
        if grid[row][i] == n or grid[i][column] == n:
            return False

    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False

    return True


def is_completed(grid):
    """
    This function checks if the puzzle is completed or not.
    it is completed when all the cells are assigned with a non-zero number.

    """
    return all(all(cell != 0 for cell in row) for row in grid)


def find_empty_location(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
backtracks=0

def sudoku(grid):
    global backtracks

    if is_completed(grid):
        return grid

    row, column = find_empty_location(grid)

    for digit in range(1, 10):
        if check_dupicate(grid, row, column, digit):
            grid[row][column] = digit

            if sudoku(grid):
                return grid
            backtracks+=1
            grid[row][column] = 0

    return False


def print_solution(grid):

    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()



grid = initial_grid
print("grid before solving: \n",np.matrix(initial_grid))
solution = sudoku(grid)
if solution:
    print("grid after solving:")
    print_solution(solution)
else:
    print("Cannot find a solution.")
print('no of backtracks: ',backtracks)
