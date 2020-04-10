#!/usr/bin/python3
import sys

def main():
	size = int(input())
	world = []

	if size == 0:
		sys.exit()
	for i in range(size):
		world.append(input())
		if len(world[i]) != size:
			print("Wrong length")
			sys.exit()
	for y in reversed(range(size)):
		for x, c in enumerate(world[y]):
			if c == '.':
				tmp_height = y
				world[tmp_height] = world[tmp_height][:x] + " " + world[tmp_height][x + 1:]
				while tmp_height < size and world[tmp_height][x] == ' ':
					tmp_height += 1
				tmp_height -= 1
				world[tmp_height] = world[tmp_height][:x] + "." + world[tmp_height][x + 1:]
	for line in world:
		print(line)

if __name__ == "__main__":
	main()