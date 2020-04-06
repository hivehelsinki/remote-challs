#!/usr/bin/python3
# Python 3.6.9

import sys

size = input()
if not (size.isdigit()):
    sys.exit('Error: Not a positive integer.')
size = int(size)

grid = []
for _ in range(size):
    row = input()
    if len(row) != size or not all(c in ' #.' for c in row):
        sys.exit('Error: Inputted row is not valid.')
    grid.append(list(row))

settled = False
while not (settled):
    settled = True
    for row in range(size - 2, -1, -1):
        for col, c in enumerate(grid[row]):
            if (c is '.' and grid[row+1][col] is ' '):
                grid[row][col] = ' '
                grid[row+1][col] = '.'
                settled = False

print('\n'.join(''.join(row) for row in grid))
