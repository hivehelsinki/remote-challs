#!/usr/bin/python3
# Python 3.6.9

import sys

def simulate(grid):
    for row in range(size - 2, -1, -1):
        for col, c in enumerate(grid[row]):
            if (c is '.' and grid[row+1][col] is ' '):
                grid[row][col] = ' '
                grid[row+1][col] = '.'
                simulate(grid)

size = input()
if not (size.isdigit()):
    sys.exit('Error: Not a positive integer.')
size = int(size)

grid = []
for _ in range(size):
    row = input()
    if len(row) != size or not all(c in ' #.' for c in row):
        sys.exit('Error: Input row is invalid.')
    grid.append(list(row))

simulate(grid)

for row in grid:
    print(''.join(row))
