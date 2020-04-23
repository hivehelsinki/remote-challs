#!/usr/bin/python3

import sys
import fileinput

def solve(lines):
	if len(lines) < 1: 
		sys.exit(sys.argv[0] + ": Can't read file")
	try:
		widths = [int(i) for i in lines[0].split()]
	except:
		sys.exit(sys.argv[0] + ": Can't read file")
	widths.sort(reverse=True)
	shelf_amount = len(widths)
	if shelf_amount < 1: 
		sys.exit(sys.argv[0] + ": Can't read file")

	iterlines = iter(lines)
	next(iterlines)

	total_width = 0
	for line in iterlines:
		book_width = line.split(' ')
		if len(book_width) < 2 or book_width[0].isdigit() == 0: 
			sys.exit(sys.argv[0] + ": Can't read file")
		total_width += int(book_width[0])
					
	needed = 0
	shelf_width = 0
	while total_width > shelf_width and needed < shelf_amount:
		shelf_width += widths[needed]
		needed += 1
	if total_width > shelf_width:
		print(sys.argv[0] + ": too_large_collection.txt: Not enough space in the given shelves")
	else:
		print (needed)

def main():	
	lines = []
	if len(sys.argv) == 1:
		try:
			for line in fileinput.input():
				lines.append(line)
		except FileNotFoundError:
			sys.exit(sys.argv[0] + ": not_existing_file: Can't read file")
		except PermissionError:
			sys.exit(sys.argv[0] + ": permission_denied_file: Can't read file")
		except:
			sys.exit(sys.argv[0] + ": Can't read file")
		solve(lines)
	else:
		iterargs = iter(sys.argv)
		next(iterargs)
		for arg in iterargs:
			lines = []
			try:
				for line in fileinput.input(arg):
					lines.append(line)
			except FileNotFoundError:
				print(sys.argv[0] + ": not_existing_file: Can't read file")
			except PermissionError:
				print(sys.argv[0] + ": permission_denied_file: Can't read file")
			except:
				print(sys.argv[0] + ": Can't read file")
			else:
				solve(lines)
	

if __name__ == "__main__":
	main()
