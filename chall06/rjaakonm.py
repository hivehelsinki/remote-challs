#!/usr/bin/python3

import sys
import fileinput

def main():	
	lines = []
	try:
		for line in fileinput.input():
			lines.append(line)
	except FileNotFoundError:
		sys.exit(sys.argv[0] + ": not_existing_file: Can't read file")
	except PermissionError:
		sys.exit(sys.argv[0] + ": permission_denied_file: Can't read file")
	except:
		sys.exit(sys.argv[0] + ": Can't read file")

	if len(lines) < 1: 
		sys.exit(sys.argv[0] + ": Can't read file")

	widths = [int(i) for i in lines[0].split() if i.isdigit()]
	widths.sort(reverse=True)
	shelf_amount = len(widths)
	if shelf_amount < 1: 
		sys.exit(sys.argv[0] + ": Can't read file")

	iterlines = iter(lines)
	next(iterlines)

	total_width = 0
	for line in iterlines:
		book_width = [int(i) for i in line.split(' ') if i.isdigit()]
		if len(book_width) < 1: 
			sys.exit(sys.argv[0] + ": Can't read file")
		if book_width and isinstance(book_width[0], int):
			total_width += book_width[0]
					
	needed = 0
	shelf_width = 0
	while total_width > shelf_width and needed < shelf_amount:
		shelf_width += widths[needed]
		needed += 1
	if total_width > shelf_width:
		print(sys.argv[0] + ": too_large_collection.txt: Not enough space in the given shelves")
	else:
		print (needed)

if __name__ == "__main__":
    main()
