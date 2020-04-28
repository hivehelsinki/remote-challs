#!/usr/bin/env python3
#Python 3.8.2
import sys
import math

def snail(lines):
    size = len(lines[0])
    i = 0
    while (i < size / 2):
        if size % 2 == 1 and i == math.floor(size / 2):
            print(lines[i][i:size-i])
            return
        
        line = list(lines[i][i:size-i])
        for c in line:
            print(c, end=', ')
        j = i + 1
        while (j < size - i - 1):
            print(lines[j][-i-1] + ',', end=' ')
            j += 1
        k = size - i - 1
        while (k > i):
            print(lines[size-1-i][k] + ',', end=' ')
            k -= 1
        if (i + 1 < size / 2):
            print(lines[size-1-i][k] + ',', end=' ')
        else:
            print(lines[size-1-i][k])
            return
        while (j > i + 1):
            j -= 1
            print(lines[j][i] + ',', end=' ')

        i += 1

def check_lines(lines):
    size = len(lines[0])
    count = 0
    for line in lines:
        if len(line) != size or not line.isdigit():
            return False
        count += 1
    return count == size

def main():
    if len(sys.argv) > 1 and check_lines(sys.argv[1:]):
        snail(sys.argv[1:])
    else:
        print('usage:', sys.argv[0], '<1-9 squared_rows...>', sep=' ')


if __name__ == "__main__":
    main()