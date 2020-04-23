#!/usr/bin/env python3

import sys, fileinput, re

def get_biggest(shelfs):
		biggest = 0
		for i in range(0, len(shelfs) - 1):
			if int(shelfs[i]) > int(shelfs[biggest]):
				biggest = i
		size = shelfs[biggest]
		del shelfs[biggest]
		return int(size)

if len(sys.argv) < 2:
	lines = []
	shelfs = input().split()
	for n in shelfs:
		if not n.isdigit():
			sys.exit(sys.argv[0] + ": " + "stdin:" + " Can't read file")
	while True:
		try:
			line = input()
		except EOFError:
			break
		lines.append(line)
	files = []
	books = 0
	for line in lines:
		try:
			books += int((re.search(r"\d+", line).group()))
		except:
			sys.exit("Invalid input")

	shelf_size = 0
	shelf_amount = 0
	while (shelf_size < books):
		shelf_size += get_biggest(shelfs)
		shelf_amount += 1
		if not shelfs:
			sys.exit(sys.argv[0] + ": " + "stdin:" + " Not enough space in the given shelves")
	print(shelf_amount)
else:
	args = sys.argv[1:]
	for arg in args:
		lines = []
		fail = 0
		if len(args) > 1:
			print(arg + ":")
		try:
			file = open(arg, "r")
		except:
			print(sys.argv[0] + ": " + arg + ": Can't read file")
			continue
		shelfs = file.readline().split()
		for n in shelfs:
			if not n.isdigit():
				print(sys.argv[0] + ": " + arg + ": Can't read file")
				fail = 1
				break
		if fail:
			continue
		for line in file:
			lines.append(line)
		files = []
		books = 0
		for line in lines:
			try:
				books += int((re.search(r"^\d+", line).group()))
			except:
				print(sys.argv[0] + ": " + arg + ": Can't read file")
				fail = 1
				break
		if fail:
			continue
		shelf_size = 0
		shelf_amount = 0
		while shelf_size < books and fail == 0:
			shelf_size += get_biggest(shelfs)
			shelf_amount += 1
			if not shelfs:
				print(sys.argv[0] + ": " + arg + ": Not enough space in the given shelves")
				fail = 1
		if fail is not 1:
			print(shelf_amount)
