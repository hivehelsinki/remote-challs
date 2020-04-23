#!/usr/bin/python3

import sys
import fileinput

def solve(lines, name):
	if len(lines) < 1: 
		print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
		return
	try:
		widths = [int(i) for i in lines[0].split()]
	except:
		print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
		return
	widths.sort(reverse=True)
	shelf_amount = len(widths)
	if shelf_amount < 1: 
		print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
		return
	iterlines = iter(lines)
	next(iterlines)
	total_width = 0
	for line in iterlines:
		book_width = line.split(' ')
		if len(book_width) < 2 or book_width[0].isdigit() == 0: 
			print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
			return
		total_width += int(book_width[0])
	needed = 0
	shelf_width = 0
	while total_width > shelf_width and needed < shelf_amount:
		shelf_width += widths[needed]
		needed += 1
	if total_width > shelf_width:
		print(sys.argv[0], ': ', name, ': Not enough space in the given shelves', sep = '')
	else:
		print (needed)

def main():	
	lines = []
	if len(sys.argv) == 1:
		for line in fileinput.input():
			lines.append(line)
		solve(lines, 'stdin')
	else:
		iterargs = iter(sys.argv)
		next(iterargs)
		for arg in iterargs:
			lines = []
			try:
				for line in fileinput.input(arg):
					lines.append(line)
			except:
				print(sys.argv[0], ": ", arg, ": Can't read file", sep = "")
			else:
				solve(lines, arg)
	

if __name__ == "__main__":
	main()
