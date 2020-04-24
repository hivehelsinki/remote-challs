#!/usr/bin/python3
import sys

READ_ERR = "Can't read file"
FIT_ERR = "Not enough space in the given shelves"

def proceed_with_error(many_args, stdin_mode, index, message):
	if many_args:
		print(f"{sys.argv[index]}:")
	if stdin_mode:
		print(f"{sys.argv[0]}: stdin: {message}")
	else:
		print(f"{sys.argv[0]}: {sys.argv[index]}: {message}")
	return (index + 1)

def book_fitter(index):
	many_args = True if len(sys.argv) > 2 else False
	stdin_mode = True if len(sys.argv) == 1 else False
	books = []
	if stdin_mode:
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
			return (proceed_with_error(many_args, stdin_mode, index, READ_ERR))
		shelves = lines[0].split()
		lines.pop(0)
		for line in lines:
			new_book = line.split()[0]
			books.append(new_book)
	elif not stdin_mode:
		try:
			with open(sys.argv[index]) as file:
				shelves = file.readline().split()		
				line = file.readline()
				while line:
					if line.split():
						new_book = line.split()[0]
					books.append(new_book)
					line = file.readline()
		except IOError as x:
			return (proceed_with_error(many_args, False, index, READ_ERR))
	try:
		shelves.sort(reverse = True, key = int)
		books.sort(reverse = True, key = int)
	except ValueError as x:
		return (proceed_with_error(many_args, stdin_mode, index, READ_ERR))
	if not shelves or not books:
		return (proceed_with_error(many_args, stdin_mode, index, READ_ERR))
	filled_shelves = []
	while books:
		if shelves:
			filled_shelves.append(int(shelves[0]))
			shelves.pop(0)
		i = 0
		while i < len(books):
			x = 0
			while x < len(filled_shelves):
				if int(books[i]) <= filled_shelves[x]:
					filled_shelves[x] -= int(books[i])
					books[i] = 'X'
					break
				x += 1
			i += 1
		if 'X' not in books:
			return (proceed_with_error(many_args, stdin_mode, index, FIT_ERR))
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
