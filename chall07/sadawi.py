#!/usr/bin/env python3

import sys

if __name__=="__main__":
	if len(sys.argv) < 2:
		sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

	arr = sys.argv[1:]

	size = len(arr[0])

	for row in arr:
		if len(row) != size or not row.isnumeric():
			sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")
	if len(arr) != size:
		sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")
	newarr = []
	for row in arr:
		row = 'a' + row + 'a'
		newarr.append(list(row))
	newarr.append(['a'] * (size + 2))
	newarr.insert(0, ['a'] * (size + 2))

	i = 1
	j = 1
	dir = 0
	sorted = []
	sorted.append(newarr[j][i])
	newarr[j][i] = 'a'
	while (1):
		moved = 0
		if dir == 0:
			while newarr[j][i+1].isnumeric():
				i += 1
				sorted.append(newarr[j][i])
				newarr[j][i] = 'a'
				moved = 1
			else:
				dir = 1
		if dir == 1:
			while newarr[j+1][i].isnumeric():
				j += 1
				sorted.append(newarr[j][i])
				newarr[j][i] = 'a'
				moved = 1
			else:
				dir = 2
		if dir == 2:
			while newarr[j][i-1].isnumeric():
				i -= 1
				sorted.append(newarr[j][i])
				newarr[j][i] = 'a'
				moved = 1
			else:
				dir = 3
		if dir == 3:
			while newarr[j-1][i].isnumeric():
				j -= 1
				sorted.append(newarr[j][i])
				newarr[j][i] = 'a'
				moved = 1
			else:
				dir = 0
		if not moved:
			break
	for i in range(0, len(sorted)):
		print(sorted[i], end="")
		if (i != len(sorted) - 1):
			print(", ", end="")
		else:
			print("")