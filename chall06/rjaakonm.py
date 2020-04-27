#!/usr/bin/python3

import sys
import fileinput

def solve(lines, name, files):
	if len(lines) < 1: 
		print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
		return
	try:
		shelf_widths = [int(i) for i in lines[0].split()]
	except:
		print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
		return
	shelf_widths.sort(reverse=True)
	shelf_amount = len(shelf_widths)
	if shelf_amount < 1: 
		print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
		return
	iterlines = iter(lines)
	next(iterlines)
	book_widths = []
	for line in iterlines:
		book_width = line.split(' ')
		if len(book_width) < 2 or book_width[0].isdigit() == 0: 
			print(sys.argv[0], ": ", name, ": Can't read file", sep = "")
			return
		book_widths.append(int(book_width[0]))
	if len(book_widths) == 0:
			if files > 1:
				print (name, ":", sep = "")
			print ("0")
			return
	book_widths.sort(reverse=True)
	for i in range(len(shelf_widths)):
		books = len(book_widths)
		j = 0
		while j < books:
			if shelf_widths[i] >= book_widths[j]:
				shelf_widths[i] -= book_widths[j]
				del book_widths[j]
				j = 0
				books -= 1
			else:
				j += 1
		if len(book_widths) == 0:
			if files > 1:
				print (name, ":", sep = "")
			print (i + 1)
			return
	print(sys.argv[0], ': ', name, ': Not enough space in the given shelves', sep = '')

def main():	
	lines = []
	if len(sys.argv) == 1:
		for line in fileinput.input():
			lines.append(line)
		solve(lines, 'stdin', 1)
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
				solve(lines, arg, len(sys.argv) - 1)
	

if __name__ == "__main__":
	main()
