#!/usr/bin/python3

import sys

if __name__ == "__main__":
	size2 = len(sys.argv) - 1
	if size2 < 1 or size2 > 20 or not all(len(sys.argv[x]) is size2 
		and sys.argv[x].isdigit() for x in range(1, size2 + 1)):
			exit(f"{sys.argv[0]}: <1-9 squared_rows...>")
	del(sys.argv[0])
	array = []
	size1 = 0
	while size1 < size2:
		for x in range(size1, size2):
			array.append(sys.argv[size1][x])
		if size2 > 1:
			for x in range(size1 + 1, size2):
				array.append(sys.argv[x][size2 - 1])
			for x in range(size2 - 2, size1 - 1, -1):
				array.append(sys.argv[size2 - 1][x])
			for x in range(size2 - 2, size1, -1):
				array.append(sys.argv[x][size1])
		size1 += 1
		size2 -= 1
	print(*array, sep = ", ")
