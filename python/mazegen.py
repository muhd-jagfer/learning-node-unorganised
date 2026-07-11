import random

WIDTH = 21   # Must be odd
HEIGHT = 21  # Must be odd

maze = [["#" for _ in range(WIDTH)] for _ in range(HEIGHT)]

directions = [
    (0, -2),
    (2, 0),
    (0, 2),
    (-2, 0)
]


def carve(x, y):
    maze[y][x] = " "

    dirs = directions[:]
    random.shuffle(dirs)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 1 <= nx < WIDTH - 1 and 1 <= ny < HEIGHT - 1:
            if maze[ny][nx] == "#":
                maze[y + dy // 2][x + dx // 2] = " "
                carve(nx, ny)


carve(1, 1)

maze[1][0] = "S"
maze[HEIGHT - 2][WIDTH - 1] = "E"

for row in maze:
    print("".join(row))