from PIL import Image

# pip install pillow
import time
import random


width = 100
heigth = 100
cellSize = 3
cols = int(width / cellSize)
rows = int(heigth / cellSize)

image = Image.new("RGB", (width + 1, heigth + 1), color="black")
pixels = image.load()

w = int(width / cellSize)
h = int(heigth / cellSize)

grid = [[0 for x in range(w)] for y in range(h)]
visited = []
stack = []
cell = 0


def move_up(x, y):
    pixels[x, y - 1] = (255, 255, 255)
    pixels[x, y - 2] = (255, 255, 255)


def move_right(x, y):
    pixels[x + 1, y] = (255, 255, 255)
    pixels[x + 2, y] = (255, 255, 255)


def move_down(x, y):
    pixels[x, y + 1] = (255, 255, 255)
    pixels[x, y + 2] = (255, 255, 255)


def move_left(x, y):
    pixels[x - 1, y] = (255, 255, 255)
    pixels[x - 2, y] = (255, 255, 255)


def setup():
    pixels[1, 1] = (0, 255, 0)
    stack.append((1, 1))
    visited.append((1, 1))
    generateMaze(1, 1)


def generateMaze(x, y):
    while len(stack) > 0:
        cells = []
        # pygame.time.wait(25)
        if (x + 2, y) not in visited and x < width - 2:
            cells.append("right")
        if (x, y + 2) not in visited and y < heigth - 2:
            cells.append("down")
        if (x - 2, y) not in visited and x > 2:
            cells.append("left")
        if (x, y - 2) not in visited and y > 2:
            cells.append("top")
        if len(cells) > 0:
            # normal move
            choice = random.randint(0, len(cells) - 1)
            if cells[choice] == "right":
                move_right(x, y)
                x, y = x + 2, y
                stack.append((x, y))
                visited.append((x, y))
                # print('right')
            if cells[choice] == "down":
                move_down(x, y)
                x, y = x, y + 2
                stack.append((x, y))
                visited.append((x, y))
                # print('down')
            if cells[choice] == "left":
                move_left(x, y)
                x, y = x - 2, y
                stack.append((x, y))
                visited.append((x, y))
                # print('left')
            if cells[choice] == "top":
                move_up(x, y)
                x, y = x, y - 2
                stack.append((x, y))
                visited.append((x, y))
                # print('top')
        else:
            # Backtrack
            x, y = stack[len(stack) - 1]
            stack.pop()
            # print('back')
            # generateMaze(x, y)
    print("ENDE")
    pixels[width - 1, heigth - 1] = (255, 0, 0)


setup()

image.save("maze.png")
