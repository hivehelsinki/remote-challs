#!/usr/bin/env python3

import sys

def main():
    length = len(sys.argv)
    if length < 2 or length > 21:
        sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

    for i in range (1, length):
        if not (len(sys.argv[i]) == (length - 1) and sys.argv[i].isdigit()):
            sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

    input_array = sys.argv[1:]

    result = []

    first_row = 0
    last_row = length - 2
    first_col = 0
    last_col = length - 2

    size = (length - 1) * (length - 1)
    k = 0
    while (k < size):
        for i in range (first_col, last_col+1):
            if (k >= size):
                break
            result.append(input_array[first_row][i])
            k+=1
        first_row += 1
        for i in range (first_row, last_row+1):
            if (k >= size):
                break
            result.append(input_array[i][last_col])
            k+=1
        last_col -= 1
        for i in range (last_col, first_col - 1, -1):
            if (k >= size):
                break
            result.append(input_array[last_row][i])
            k+=1
        last_row -= 1
        for i in range (last_row, first_row - 1, -1):
            if (k >= size):
                break
            result.append(input_array[i][first_col])
            k+=1
        first_col += 1

    print(', '.join(result))

if __name__ == "__main__":
    main()
