#!/usr/bin/env python3
import sys
import re

rows = sys.argv[1:]
size = len(rows)
p = re.compile('[1-9]+$')
comma = ", "

def usage(code):
	print(f'usage: {sys.argv[0]} <1-9 squared_rows...>')
	exit(code)

def top():
	res = ""
	for x in rows[0]:
		res += x + comma
	del rows[0]
	return res

def right(size):
	res = ""
	for y, row in enumerate(rows):
		res += row[size - 1] + comma
		rows[y] = row[:size-1]
	return res

def bottom():
	res = ""
	x = len(rows)-1
	while x >= 0:
		res += rows[len(rows)-1][x] + comma
		x-=1
	del rows[len(rows)-1]
	return res

def left():
	res = ""
	for y, row in enumerate(rows):
		res += row[0] + comma
		rows[y] = row[1:]
	return res

def check_quit(output):
	if len(rows) == 0:
		print(output[:-2])
		exit(0)

def worm(size, output):
	output += top()
	check_quit(output)

	output += right(size)
	check_quit(output)

	output += bottom()
	check_quit(output)

	output += left()
	check_quit(output)
	worm(len(rows), output)

def main():
	if size == 0:
		usage(0)
	for row in rows:
		if not p.match(row) or size != len(row):
			usage(1)
	worm(size, "")

if __name__ == "__main__":
	main()
