#!/usr/bin/env python3

import sys

def validate(lines):
	shelves = lines[0].split(' ')
	if any([not shelf.isnumeric() for shelf in shelves]):
		return "", "", False
	collections = [line.split(' ')[0] for line in lines[1:]]
	if not collections or any([not collection.isnumeric() for collection in collections]):
		return "", "", False
	shelves = [int(i) for i in shelves]
	collections = [int(i) for i in collections]
	return shelves, collections, True

def read_contents(source, stdin):
	if (stdin):
		try:
			lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
		except:
			return False
	else:
		try:
			fo = open(source, 'r')
			lines = [line.rstrip('\n') for line in fo.readlines()]
			fo.close()
		except:
			return False
	return lines

def fit_books(progname, source, stdin):
	lines = read_contents(source, stdin)
	if "/" in source:
		source = source.rpartition('/')[2]
	if not lines:
		print(f"{progname}: {source}: Can't read file")
		return
	shelves, collections, valid = validate(lines)
	if not valid:
		print(f"{progname}: {source}: Can't read file")
		return
	shelves.sort(reverse=True)
	books_total = sum(collections)
	shelves_needed = 0
	shelves_total = len(shelves)
	while books_total > 0:
		if shelves_needed == shelves_total:
			print(f"{progname}: {source}: Not enough space in the given shelves")
			return
		books_total -= shelves[shelves_needed]
		shelves_needed += 1
	print(shelves_needed)

def main():
	args = len(sys.argv)
	if args == 2:
		fit_books(sys.argv[0], sys.argv[1], False)
	elif args > 2:
		for file in sys.argv[1:]:
			print(f"{file}:")
			fit_books(sys.argv[0], file, False)
			if args > 2:
				print("")
			args -= 1
	else:
		fit_books(sys.argv[0], "stdin", True)

if __name__ == "__main__":
	main()
