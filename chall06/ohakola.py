#!/usr/bin/python3
import sys

def shelves_count_try(books, shelves, shelf_index, book_index):
	count = 1
	curr_shelf = shelves[shelf_index]
	books_len = len(books)
	for _ in range(books_len):
		if curr_shelf >= books[book_index]:
			curr_shelf = curr_shelf - books[book_index]
			book_index += 1
			if book_index >= books_len:
				book_index = 0
		else:
			count += 1
			if count >= len(shelves):
				print("stdin: Not enough space in the given shelves")
				exit()
			shelf_index += 1
			if shelf_index >= len(shelves):
				shelf_index = 0
			curr_shelf = shelves[shelf_index]
	return count

def variable_bin_pack(books, shelves):
	result = 999999999
	for j in range(len(books)):
		for i in range(len(shelves)):
			try_count = shelves_count_try(books, shelves, i, j)
			if try_count < result:
				result = try_count
	return result

if __name__ == "__main__":
	lines = sys.stdin.readlines()
	try:
		shelves = lines.pop(0).split(" ")
		for i, s in enumerate(shelves):
  			shelves[i] = int(s.rstrip())
	except:
		print("Wrong shelves given")
		exit()
	try:
		books = []
		for b in lines:
			book = b.split(" ")
			books.append(int(book[0]))
	except:
		print("Wrong books given")
		exit()
	print(variable_bin_pack(books, shelves))
