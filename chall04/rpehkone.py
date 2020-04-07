#!/usr/bin/python3
import sys
import string

size = sys.argv[1]
while 42:
	diff = 0
	for y in range(int(size)):
		for x in range(int(size)):
			if sys.argv[2 + y][x] == '.':
				if y + 1 < int(size) and sys.argv[3 + y][x] == ' ':
					sys.argv[2 + y] = sys.argv[2 + y][:x] + ' ' + sys.argv[2 + y][x + 1:]
					sys.argv[3 + y] = sys.argv[3 + y][:x] + '.' + sys.argv[3 + y][x + 1:]
					diff = 1
	if diff == 0:
		break
for i in range(int(size)):
	print(sys.argv[2 + i])
