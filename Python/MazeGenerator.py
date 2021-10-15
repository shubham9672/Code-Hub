import pygame
import time
import random

cellSize = 40
notFinished = True

width = 800
heigth = 800
cols = int(width / cellSize)
rows = int(heigth / cellSize)

w = int(width / cellSize)
h = int(heigth / cellSize)

grid = [[0 for x in range(w)] for y in range(h)]
visited = []
stack = []
cell = 0


class Cell:
    def __init__(self, cellSize, x, y):
        self.cellSize = cellSize
        self.x = x
        self.y = y


def move_up(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (x * cellSize + 1, (y - 1) * cellSize + 1, cellSize - 1, (cellSize * 2 - 1)),
        0,
    )
    pygame.display.update()


def move_right(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (x * cellSize + 1, y * cellSize + 1, (cellSize * 2) - 2, cellSize - 2),
        0,
    )
    pygame.display.update()


def move_down(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (x * cellSize + 1, y * cellSize + 1, cellSize - 1, (cellSize * 2 - 1)),
        0,
    )
    pygame.display.update()


def move_left(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        ((x - 1) * cellSize + 1, y * cellSize + 1, cellSize * 2 - 2, cellSize - 1),
        0,
    )
    pygame.display.update()


def setup():
    pygame.init()
    window = pygame.display.set_mode((width, heigth))
    clock = pygame.time.Clock()
    window.fill((0, 0, 0))

    for y in range(0, cols):

        for x in range(0, rows):
            cell = Cell(cellSize, x, y)
            grid[x][y] = cell
            pygame.draw.line(
                window,
                (255, 255, 255),
                [x * cellSize, y * cellSize],
                [(x + cellSize) * cellSize, y * cellSize],
            )
            pygame.draw.line(
                window,
                (255, 255, 255),
                [(x + cellSize) * cellSize, y * cellSize],
                [(x + cellSize) * cellSize, (y + cellSize) * cellSize],
            )
            pygame.draw.line(
                window,
                (255, 255, 255),
                [(x + cellSize) * cellSize, (y + cellSize) * cellSize],
                [(x * cellSize), (y + cellSize) * cellSize],
            )
            pygame.draw.line(
                window,
                (255, 255, 255),
                [x * cellSize, (y + cellSize) * cellSize],
                [(x * cellSize), y * cellSize],
            )
            pygame.display.update()

    time.sleep(1)

    stack.append((0, 0))
    visited.append((0, 0))
    generateMaze(window, clock, 0, 0)
    pygame.time.wait(5000)


def generateMaze(window, clock, x, y):
    while len(stack) > 0:
        cells = []
        # pygame.time.wait(25)
        if (x + 1, y) not in visited and x < cols - 1:
            cells.append("right")
        if (x, y + 1) not in visited and y < rows - 1:
            cells.append("down")
        if (x - 1, y) not in visited and x > 0:
            cells.append("left")
        if (x, y - 1) not in visited and y > 0:
            cells.append("top")
        if len(cells) > 0:
            # normal move
            choice = random.randint(0, len(cells) - 1)
            if cells[choice] == "right":
                move_right(window, x, y)
                x, y = x + 1, y
                stack.append((x, y))
                visited.append((x, y))
            if cells[choice] == "down":
                move_down(window, x, y)
                x, y = x, y + 1
                stack.append((x, y))
                visited.append((x, y))
            if cells[choice] == "left":
                move_left(window, x, y)
                x, y = x - 1, y
                stack.append((x, y))
                visited.append((x, y))
            if cells[choice] == "top":
                move_up(window, x, y)
                x, y = x, y - 1
                stack.append((x, y))
                visited.append((x, y))
        else:
            # Backtrack
            x, y = stack[len(stack) - 1]
            stack.pop()
            # print('back')
            # generateMaze(window, x, y)
        clock.tick(60)


def pickCell(window, x, y):
    pygame.draw.rect(
        window,
        (0, 255, 0),
        (x * cellSize + 2, y * cellSize + 2, cellSize - 4, cellSize - 4),
        0,
    )
    pygame.display.update()


setup()
