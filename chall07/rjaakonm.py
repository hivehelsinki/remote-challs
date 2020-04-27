#!/usr/bin/python3

import sys

def Reverse(lst): 
    lst.reverse() 
    return lst

def PrintAndDelete(array, new_array):
	rows = len(array)
	columns = len(array[0])
	first = array[0]
	if rows > 1:
		last = Reverse(array[rows - 1])

	for x in first:
		new_array.append(x)
	if rows > 2:
		for x in range(1, rows - 1):
			new_array.append(array[x][columns - 1])
			del(array[x][columns - 1])
	if rows > 1:
		for x in last:
			new_array.append(x)
	if rows > 2 and columns > 1:
		for x in range(rows - 2, 0, -1):
			new_array.append(array[x][0])
			del(array[x][0])
	if rows > 1:
		del(array[rows - 1])
	del(array[0])

def main():
	if len(sys.argv) > 1:
		array = []
		for x in range(1, len(sys.argv)):
			temp = []
			if len(sys.argv[x]) is not len(sys.argv) - 1:
				exit(f"{sys.argv[0]}: <1-9 squared_rows...>")
			for y in range(len(sys.argv[x])):
				if sys.argv[x][y] >= '0' and sys.argv[x][y] <= '9':
					temp.append(ord(sys.argv[x][y]) - 48)
				else:
					exit(f"{sys.argv[0]}: <1-9 squared_rows...>")
			array.append(temp)
	else:
		exit(f"{sys.argv[0]}: <1-9 squared_rows...>")

	new_array = []
	while len(array) > 0:
		PrintAndDelete(array, new_array)
	print(*new_array, sep = ", ")  

if __name__ == "__main__":
	main()