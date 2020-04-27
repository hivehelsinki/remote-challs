#!/usr/bin/env python3
# 3.6.9
import sys

def to_int(value):
	try:
		num = int(value)
	except ValueError:
		print("argument was wrong type")
		sys.exit(1)
	return num


# Remove newlines and first row, append spaces to rows
def normalize(grid, size):
	# Feeling Go
	for y, row in enumerate(grid):
		row = row[:size]
		grid[y] = row.replace("\n", "")
		row_len = len(grid[y])
		while row_len < size:
			grid[y] += " "
			row_len += 1
	return grid[1:]

def swap(str, old, new):
    return str[:old] + new + str[old + 1:]

def handle_swap(grid, size, y, x):
	if grid[y][x] == " " and grid[y - 1][x] == ".":
		grid[y] = swap(grid[y], x, ".")
		grid[y-1] = swap(grid[y-1], x, " ")
		return True
	return False

def skyfall(grid, size):
	y, x = size, size
	while x >= 0:
		while y > 0:
			if handle_swap(grid, size, y, x):
				y = size
			else:
				y -= 1
		y = size
		x -= 1
	return grid[:size+1]


def main():
	grid = []
	for line in sys.stdin:
		grid.append(line)
	size = to_int(grid[0])
	print(*skyfall(normalize(grid, size), size - 1), sep='\n')

if __name__ == "__main__":
	main()
