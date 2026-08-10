import random
import os
import time

WIDTH = 15
HEIGHT = 12

player = WIDTH // 2
rocks = []
score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    # Create a new rock
    if random.random() < 0.5:
        rocks.append([random.randint(0, WIDTH - 1), 0])

    # Move rocks down
    new_rocks = []
    for rock in rocks:
        rock[1] += 1
        if rock[1] < HEIGHT:
            new_rocks.append(rock)
    rocks = new_rocks

    # Collision check
    for x, y in rocks:
        if y == HEIGHT - 1 and x == player:
            clear()
            print("💥 GAME OVER!")
            print("Score:", score)
            exit()

    # Draw screen
    clear()
    print("DODGE THE ROCKS")
    print("Move: A = Left, D = Right")
    print("Score:", score)
    print("-" * (WIDTH + 2))

    for y in range(HEIGHT):
        line = "|"
        for x in range(WIDTH):
            if y == HEIGHT - 1 and x == player:
                line += "A"
            elif any(rx == x and ry == y for rx, ry in rocks):
                line += "*"
            else:
                line += " "
        line += "|"
        print(line)

    print("-" * (WIDTH + 2))

    move = input("Move: ").lower()

    if move == "a" and player > 0:
        player -= 1
    elif move == "d" and player < WIDTH - 1:
        player += 1

    score += 1
    time.sleep(0.1)