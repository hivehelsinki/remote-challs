#!/usr/bin/env python3
# Python3 snake

import sys

# Rotate Matrix by 90 Degrees Counter-ClockWise
def rotate_matrix( matrix ):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

# Print Only first raw of Matrix
# Adds a ", " if there is more row to print 
def printTop(arr, rows):
    i = 0
    for j in range(len(arr[i])):
        print(arr[i][j], end='')
        if rows > 1:
            print(", ", end='')
        else:
            print ()

# Validates input
# Must Contain only numeric valiue
# Must be a square
def validateInput():
    for row in sys.argv:
        if len(sys.argv) != len(row) or not(row.isnumeric()):
            return 1
    return 0

# Print first raw of the Matrix
# Remove first raw
# If there is more than one row
# -> Rotate Counter ClockWise by 90 Degree
# Set the number of rows using the new matrix
# Repeat
def main():
    name = str(sys.argv[0])
    matrix = sys.argv
    matrix.pop(0)
    rows = len(matrix)
    if validateInput() or len(sys.argv) < 1:
        print("usage: " + name + " <1-9 squared_rows...>")
    else:
        while rows > 0:
            printTop(matrix, rows)
            matrix.pop(0)
            if rows > 1:
                matrix = rotate_matrix(matrix)
            rows = len(matrix)

if __name__ == "__main__":
	main()