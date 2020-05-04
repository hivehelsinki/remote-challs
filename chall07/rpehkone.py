#!/usr/bin/python3

import sys

def usage():
	print("usage: " + sys.argv[0] + " <1-9 squared_rows...>")
	exit()

def main():
	if (len(sys.argv) == 1):
		usage()
	for i in range(len(sys.argv) - 1):
		if (len(sys.argv) - 1 != len(sys.argv[i + 1])):
			usage()
		for j in range(len(sys.argv[i + 1])):
			num = sys.argv[i + 1][j]
			if num < '0' or num > '9':
				usage()
	size = len(sys.argv[1]) - 1
	x = 0
	y = 0
	edge = 0;
	while edge <= size / 2:
		while x < size - edge:
			print(sys.argv[y + 1][x] + ", ", end="")
			x = x + 1
		while y < size - edge:
			print(sys.argv[y + 1][x] + ", ", end="")
			y = y + 1
		while x > 0 + edge:
			print(sys.argv[y + 1][x] + ", ", end="")
			x = x - 1
		edge = edge + 1
		while y > 0 + edge:
			print(sys.argv[y + 1][x] + ", ", end="")
			y = y - 1
	print(sys.argv[y + 1][x])

if __name__ == "__main__":
	main()
