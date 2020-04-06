#!/usr/bin/python3

size = int(input())
grid = []

for i in range(size):
    grid.append(list(input()))

def can_move(next_under):
    if (next_under == ' '):
        return True
    return False

moved = True
while moved:
    moved = False
    for row in range(size):
        for col in range(size):
            if (grid[row][col] == '.'):
                if (row + 1 < size and can_move(grid[row + 1][col])):
                    grid[row][col] = ' '
                    grid[row + 1][col] = '.'

for i in grid:
    for j in i:
        print(j, end="")
    print()
