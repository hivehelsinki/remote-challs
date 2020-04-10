#!/usr/bin/python3.7

import sys

def falling_sand(input_array):
    length = len(input_array)
    y = 0
    while y < length:
        x = 0
        while x < length:
            if input_array[y][x] == '.' and y < length - 1 and input_array[y + 1][x] == ' ':
                input_array[y + 1][x] = '.'
                input_array[y][x] = ' '
            x += 1
        y += 1
    for raw in input_array:
        print(''.join(raw))

def is_valid(input_str, length):
    if (len(input_str) != length):
        return False
    for char in input_str:
        if char != ' ' and char != '.' and char != '#':
            return False
    return True

def main():
    input_array = []
    try:
        length = int(input())
    except:
        print("\033[91mNot valid integer!\033[0m")
        sys.exit(1)
    count = length
    while count > 0:
        input_str = input()
        if not is_valid(input_str, length):
            print("\033[91mNot correct input!\033[0m")
            sys.exit(1)
        input_array.append(list(input_str))
        count -= 1
    falling_sand(input_array)

if __name__ == "__main__":
    main()

