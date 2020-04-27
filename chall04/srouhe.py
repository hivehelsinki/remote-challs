#!/usr/bin/python3
import sys


class SandDealer():
	def __init__(self):
		self.size = self.parse_size()
		self.world = self.parse_world()

	def drop_sand(self):
		for x in range(0, self.size):
			self.drop_one(x)	

	def drop_one(self, x):
		for y in range(0, self.size - 1):
			if self.world[y][x] == '.' and self.world[y + 1][x] == ' ':
				self.world[y][x] = ' '
				self.world[y + 1][x] = '.'
			else:
				break

	def print_world(self):
		sep = ''
		for line in self.world:
			s = sep.join(line)
			print(s)

	# Preprocessing
	def parse_world(self):
		world = []
		try:
			for i, line in enumerate(sys.stdin):
				world.append(self.check_chars(line, self.size))
				if i > self.size - 2:
					break
		except Exception as e:
			print(f'Error parsing input: [{e}]')
			exit(1)
		return world

	# Preprocessing
	def check_chars(self, line, size):
		line = self.split(line.replace('\n', ''))
		if len(line) != size:
			print(f'Invalid line length')
			exit(1)
		for c in line:
			if c not in '. #':
				print(f'Invalid character `{c}`')
				exit(1)
		return line

	# Preprocessing
	def parse_size(self):
		try:
			for line in sys.stdin:
				return int(line)
		except Exception as e:
			print(e)
			exit(1)

	# Utility
	def split(self, word): 
		return [char for char in word]




if __name__ == '__main__':

	world = SandDealer()
	if world.size is not None and world.world != []:
		world.drop_sand()
		world.print_world()

