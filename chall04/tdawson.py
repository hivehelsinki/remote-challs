#!/usr/bin/python3
#Python 3.6.9

import sys

n = int(input())
grid = []

for _ in range (n):
    grid.append(list(input()))

settled = False
while (not settled):
    settled = True
    for i in range(n - 2, -1, -1):
        for j, c in enumerate(grid[i]):
            if (c is '.' and grid[i+1][j] is ' '):
                settled = False
                grid[i+1][j], grid[i][j] = grid[i][j], grid[i+1][j]


for row in grid:
    print(''.join(row))
