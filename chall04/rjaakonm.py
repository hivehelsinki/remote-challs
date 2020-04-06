#!/usr/bin/python3

import sys

def main():
	lines = []
	counted = 0
	for line in sys.stdin:
		lines.append(list(line))
		counted += 1
	lines[0] ="".join(lines[0])
	try:
		size = int(lines[0])
	except:
		return
	if size == counted - 1:
		i = 1
		while i < size:
			j = 0
			while j < size:
				if lines[i][j] == '.' and lines[i + 1][j] == ' ':
					lines[i][j] = ' '
					lines[i + 1][j] = '.'
				elif lines[i][j] != '.' and lines[i][j] != '#' and lines[i][j] != ' ':
					return
				j += 1
			if lines[i][j] != '\n' and lines[i][j] != '\0':
				return
			lines[i] = "".join(lines[i])
			i += 1
		lines[size] = "".join(lines[size])
		i = 1
		while i <= size:
			print(lines[i])
			i += 1

if __name__ == "__main__":
    main()
