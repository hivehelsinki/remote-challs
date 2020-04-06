import sys

def map_error_exit(msg):
	print(f"Error occured: {msg}")
	exit()

class FallingSand():
	def __init__(self, size, raw):
		self.size = size
		self.map = list()
		self.setup(raw)
	
	def __str__(self):
		res = ""
		for row in self.map:
			for c in row:
				res += c
			res += '\n'
		return res.rstrip('\n')

	def setup(self, raw):
		for line in raw:
			clean = line.rstrip('\n')
			l = len(clean)
			if l != n:
				map_error_exit(f"Invalid lenght of a line len(\'{clean}\') = {l} != {self.size}")
			row = list()
			for i in range(l):
				if not line[i] in " .#":
					map_error_exit("Invalid Characters")
				row.append(line[i])
			self.map.append(row)
	
	def simulate(self):
		change = True
		while change:
			change = False
			i = self.size - 1
			while i > 0:
				k = self.size - 1
				while k >= 0:
					if self.map[i][k] == ' ' and self.map[i - 1][k] == '.':
						self.map[i][k] = '.'
						self.map[i - 1][k] = ' '
						change = True
					k -= 1
				i -= 1


if __name__ == "__main__":
	raw = sys.stdin.readlines()
	try:
		n = int(raw[0].rstrip())
	except:
		map_error_exit("Given N is not an integer")
	else:
		if len(raw) - 1 != n:
			map_error_exit("Given map is not N sized")
	sim = FallingSand(n, raw[1:])
	sim.simulate()
	print(sim)
