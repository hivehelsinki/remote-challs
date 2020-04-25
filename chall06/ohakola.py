#!/usr/bin/python3
import sys

# Loops through books and tries to fit them to shelves
# If count goes too high, return -1
def shelves_needed(books, shelves, shelf_index, book_index):
	count = 1
	curr_shelf = shelves[shelf_index]
	books_len = len(books)
	shelves_len = len(shelves)
	books_placed = 0
	while books_placed < books_len:
		if curr_shelf >= books[book_index]:
			curr_shelf = curr_shelf - books[book_index]
			book_index += 1
			if book_index >= books_len:
				book_index = 0
			books_placed += 1
		else:
			count += 1
			if count > shelves_len:
				return -1
			shelf_index += 1
			if shelf_index >= shelves_len:
				shelf_index = 0
			curr_shelf = shelves[shelf_index]
	return count

# Sorts shelves from largest to smalles after which attempt shelves_needed
# function for each book index and for each shelf index
# returns best solution
def variable_shelf_pack(books, shelves, program, source):
	MAX_INT = 999999999
	result = MAX_INT
	if len(books) == 0:
		return 0
	if sum(books) > sum(shelves):
		print(f"{program}: {source}: Not enough space in the given shelves")
		exit()
	shelves.sort(key=int, reverse=True)
	for j in range(len(books)):
		for i in range(len(shelves)):
			try_count = shelves_needed(books, shelves, i, j)
			if try_count != -1 and try_count < result:
				result = try_count
	if result == MAX_INT:
		print(f"{program}: {source}: Not enough space in the given shelves")
		exit()
	return result

if __name__ == "__main__":
	program = sys.argv[0]
	source = "stdin"
	arg_len = len(sys.argv)
	if arg_len == 2:
		source = sys.argv[1]
		try:
			with open(sys.argv[1]) as f:
				lines = f.readlines()
		except:
			print(f"{program}: {source}: No such file")
			exit()
	elif arg_len == 1:
		lines = sys.stdin.readlines()
	else:
		print(f"{program}: Too many args, only one file accepted")
		exit()
	try:
		shelves = lines.pop(0).split(" ")
		for i, s in enumerate(shelves):
  			shelves[i] = int(s.rstrip())
	except:
		print(f"{program}: {source}: Invalid shelf input given")
		exit()
	try:
		books = []
		for b in lines:
			book = b.split(" ")
			books.append(int(book[0]))
	except:
		print(f"{program}: {source}: Invalid books input given")
		exit()
	print(variable_shelf_pack(books, shelves, program, source))
