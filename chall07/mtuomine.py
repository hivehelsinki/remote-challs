#!/usr/bin/env python3
import sys
import re

rows = sys.argv[1:]
size = len(rows)
p = re.compile('[1-9]+$')
comma = ", "

def usage():
	exit(f'usage: {sys.argv[0]} <1-9 squared_rows...>')

def top():
	res = ""
	for x in rows[0]:
		res += x + comma
	del rows[0]
	return res

def right():
	res = ""
	width = len(rows[0]) - 1
	for y, row in enumerate(rows):
		res += row[width] + comma
		rows[y] = row[:width]
	return res

def bottom():
	res = ""
	last = len(rows)-1
	x = last
	while x >= 0:
		res += rows[last][x] + comma
		x-=1
	del rows[last]
	return res

def left():
	res = ""
	for y, row in enumerate(rows):
		res += " ," + row[0]
		rows[y] = row[1:]
	return res[::-1]

def check_quit(output):
	if len(rows) == 0:
		print(output[:-2])
		exit(0)

def cut(funcs, output):
	for func in funcs:
		output += func()
		check_quit(output)
	cut(funcs, output)

if __name__ == "__main__":
	if size == 0 or size > 20:
		usage()
	for row in rows:
		if not p.match(row) or size != len(row):
			usage()
	cut([top, right, bottom, left], "")
