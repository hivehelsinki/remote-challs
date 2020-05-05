#!/usr/bin/python3
import sys
import enum

class Direction(enum.Enum):
	right = 0
	down = 1
	left = 2
	up = 3

def turn_direction(dir):
	val = dir.value + 1
	if val > 3:
		val = 0
	return Direction(val)

def step_xy(dir, x, y):
	switcher={
		Direction.right: (x + 1, y),
		Direction.down: (x, y + 1),
		Direction.left: (x - 1, y),
		Direction.up: (x, y - 1),
	}
	return switcher.get(dir, "Invalid direction")

def snail_traverse(grid, size):
	snail_path = []
	x, y = 0, 0
	step = 0
	step_limit = size - 1
	turn_limit = 3
	turns = 0
	dir = Direction.right
	snail_path.append(str(grid[y][x]))
	for i in range(size * size - 1):
		x, y = step_xy(dir, x, y)
		snail_path.append(str(grid[y][x]))
		step += 1
		if step == step_limit:
			dir = turn_direction(dir)
			turns += 1
			step = 0
		if turns == turn_limit:
			if turn_limit == 3:
				turn_limit = 2
			step_limit -= 1
			turns = 0
	return ", ".join(snail_path)

def parse_grid(args, size):
	grid = []
	for (i, arg) in enumerate(args):
		if i > 0:
			row = []
			for c in arg.rstrip():
				row.append(int(c))
			if len(row) != size:
				raise
			grid.append(row)
	return grid

if __name__ == "__main__":
	program = sys.argv[0]
	size = len(sys.argv) - 1
	if size > 1:
		try:
			grid = parse_grid(sys.argv, size)
		except:
			exit(f"{program}: <1-9 squared_rows...>")
	else:
		exit(f"{program}: <1-9 squared_rows...>")
	print(snail_traverse(grid, size))
