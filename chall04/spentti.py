#!/usr/bin/env python3

print('input:')
n = int(input())
grid = []

for row in range(n):
	grid.append(list(input()))

for y in range(n):
	for x in range(n):
		if grid[n - y - 1][x] == '.':
			y2 = n - y - 1
			while y2 + 1 < n and grid[y2 + 1][x] == ' ':
				grid[y2][x] = ' '
				grid[y2 + 1][x] = '.'
				y2 += 1

print('\noutput:')
for row in grid:
	print(''.join(map(str, row)))
