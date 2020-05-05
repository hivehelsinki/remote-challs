#!/usr/bin/env python3

import sys

def print_usage(progname):
	print(f"usage: {progname} <1-9 squared_rows...>")
	exit()

def validate(args, size):
	if size < 1 or size > 20:
		print_usage(sys.argv[0])
	if any([not line.isnumeric() or len(line) != size for line in args[1:]]):
		print_usage(sys.argv[0])

def top(result, array):
	if array:
		result += array.pop(0)
	return result, array

def right(result, array):
	if array:
		for i in range(len(array)):
			result += array[i][-1]
			array[i] = array[i][:-1]
	return result, array

def bottom(result, array):
	if array:
		result += array.pop()[::-1]
	return result, array

def left(result, array):
	if array:
		result += "".join(line[0] for line in array)
		for i in range(len(array)):
			array[i] = array[i][1:]
	return result, array

def snail(array):
	result = ""
	while array:
		result, array = top(result, array)
		result, array = right(result, array)
		result, array = bottom(result, array)
		result, array = left(result, array)
	return result

if __name__ == "__main__":
	validate(sys.argv, len(sys.argv) - 1)
	result = snail(sys.argv[1:])
	print(", ".join(c for c in result))
