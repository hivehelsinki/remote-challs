#!/usr/bin/python3
import sys

READ_ERR = "Can't read file"
FIT_ERR = "Not enough space in the given shelves"

def print_proceed(many_args, std_input, index, message):
	if many_args:
		print(f"{sys.argv[index]}:")
	if std_input:
		print(f"{sys.argv[0]}: stdin: {message}")
	else:
		print(f"{sys.argv[0]}: {sys.argv[index]}: {message}")
	return (index + 1)

def book_fitter(index):
	many_args = len(sys.argv) > 2
	std_input = len(sys.argv) == 1
	books = []
	if std_input:
		lines = []
		while True:
			try:
				std_line = input()
				if std_line == '':
					break
				lines.append(std_line)
			except EOFError:
				break
		if not lines:
			return (print_proceed(many_args, std_input, index, READ_ERR))
		shelves = lines[0].split()
		lines.pop(0)
		for line in lines:
			new_book = line.split()[0]
			books.append(new_book)
	elif not std_input:
		try:
			with open(sys.argv[index]) as open_file:
				shelves = open_file.readline().split()		
				line = open_file.readline()
				while line:
					if line.split():
						new_book = line.split()[0]
					books.append(new_book)
					line = open_file.readline()
		except IOError:
			return (print_proceed(many_args, False, index, READ_ERR))
	try:
		shelves.sort(reverse = True, key = int)
		books.sort(reverse = True, key = int)
	except ValueError:
		return (print_proceed(many_args, std_input, index, READ_ERR))
	if not shelves or not books:
		return (print_proceed(many_args, std_input, index, READ_ERR))
	filled_shelves = []
	while books:
		if shelves:
			filled_shelves.append(int(shelves[0]))
			shelves.pop(0)
		i = 0
		while i < len(books):
			j = 0
			while j < len(filled_shelves):
				if int(books[i]) <= filled_shelves[j]:
					filled_shelves[j] -= int(books[i])
					books[i] = 'X'
					break
				j += 1
			i += 1
		if 'X' not in books:
			return (print_proceed(many_args, std_input, index, FIT_ERR))
		books[:] = (value for value in books if value != 'X')
	if many_args:
		print(f"{sys.argv[index]}:")
	print(len(filled_shelves))
	return (index + 1)

def main():
	index = book_fitter(1)
	while (index < len(sys.argv)):
		print("")
		index = book_fitter(index)

if __name__ == "__main__":
	main()
