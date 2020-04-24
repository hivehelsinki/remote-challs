#!/usr/bin/python3
import sys

def shelves_count_try(books, shelves, shelf_index):
	count = 0
	tmp = shelves[shelf_index]
	for i in range(len(books)):
		if tmp >= books[i]:
			tmp = tmp - books[i]
		else:
			count += 1
			if count >= len(shelves):
				print("stdin: Not enough space in the given shelves")
				exit()
			shelf_index += 1
			if shelf_index >= len(shelves):
				shelf_index = 0
			tmp = shelves[shelf_index] - books[i]
	return count

def variable_bin_pack(books, shelves):
	result = sys.maxint
	for i in range(shelves):
		try_count = shelves_count_try(books, shelves, i)
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
	print(books)
	print(variable_bin_pack(books, shelves))
