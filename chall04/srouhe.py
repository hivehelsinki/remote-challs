#!/usr/bin/python3

import sys

def split(word): 
    return [char for char in word]

def parse_stdin():
	world = []
	count = 0
	try:
		for line in sys.stdin:
			if count == 0:
				size = int(line)
			elif count <= size:
				world.append(split(line.replace('\n', '')))
			count += 1
	except Exception as e:
		print(f'Error parsing input: [{e}]')
		exit(1)
	return size, world

def check_chars(c1, c2):
	if c1 not in '. #' or c2 not in '. #':
		print('Invalid character')
		exit(1)

def sand_dealer(size: int, world: list):
	for y in range(0, size - 1):
		for x in range(0, size):
			check_chars(world[y][x], world[y + 1][x])
			if world[y][x] == '.' and world[y + 1][x] == ' ':
				world[y][x] = ' '
				world[y + 1][x] = '.'
	return world

def print_world(result: list):
	sep = ''
	for line in result:
		s = sep.join(line)
		print(s)


if __name__ == '__main__':

	size, world = parse_stdin()
	result = sand_dealer(size, world)
	print_world(result)
