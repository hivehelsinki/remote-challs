#!/usr/bin/python3
# Version 3.6.8

import sys

def validate_input(lines):
	if len(lines) == 0:
		return 0
	dim = lines.pop(0)
	if not dim.isnumeric():
		return 0
	dim = int(dim)
	if len(lines) != dim:
		return 0
	for line in lines:
		if len(line) != dim:
			return 0
		for c in line:
			if not c in " .#":
				return 0
	return dim

def convert_lines(lines, dim):
	"Changes list lines from horizontal to vertical"
	i = 0
	converted_lines = []
	while i < dim:
		converted_lines.append("".join(line[i] for line in lines))
		i += 1
	return converted_lines

def fall_sand(vlines):
	"Simulates falling of sand for each line"
	fallen_lines = []
	for line in vlines:
		i = 0
		splitted = line.split('#')
		for part in splitted:
			splitted[i] = part.replace(" ", "").rjust(len(part), " ")
			i += 1
		fallen_lines.append("#".join(splitted))
	return fallen_lines

lines = []
for line in sys.stdin.readlines():
	lines.append(line.rstrip('\n'))
dim = validate_input(lines)
if dim == 0:
	exit("Invalid input")
vertical_lines = convert_lines(lines, dim)
fallen_lines = fall_sand(vertical_lines)
lines = convert_lines(fallen_lines, dim)
for line in lines:
	print(line)
