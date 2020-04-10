#!/usr/bin/env python3
# python 3.7.4 Windows 10

import sys


def input_error():
    print("Bad input, n > 0 and only '.' ' ' and '#' allowed")
    exit(-1)


def main():
    lines = []
    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    if n < 1:
        input_error()
    lines.pop(0)

    print("\n:::START POSITION:::\n")
    print("N =", n)
    for line in lines:
        print(line)
    print("--------------------")

    for i in range(n):
        for j in range(n):
            if lines[i][j] is '.' and lines[i + 1][j] is ' ':
                lines[i][j] = ' '
                lines[i + 1][j] = '.'


if __name__ == "__main__":
    main()
