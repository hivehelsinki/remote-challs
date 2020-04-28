#!/usr/bin/env python3
# python 3.8.2 Windows 10

import sys


def validate(lines, n):

    for row in lines:
        if len(row) != n:
            sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")
        for column in row:
            if column.isdigit() is False:
                sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

    if n > 20:
        sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")


def top(min_line, lines, ret):
    if not lines:
        return
    for i in range(len(lines)):
        ret.append(lines[min_line][i])
    lines.pop(min_line)
    return lines, ret


def right(lines, ret):
    if not lines:
        return
    for i in range(len(lines)):
        ret.append(lines[i][-1])
        lines[i] = lines[i][:-1]
    return lines, ret


def bottom(max_line, lines, ret):
    if not lines:
        return
    lines[max_line] = lines[max_line][::-1]
    for i in range(len(lines)):
        ret.append(lines[max_line][i])
    lines.pop(max_line)
    return lines, ret


def left(min_line, max_line, lines, ret):
    if not lines:
        return
    while min_line <= max_line:
        ret.append(lines[max_line][min_line])
        lines[max_line] = lines[max_line][1:]
        max_line -= 1
    return lines, ret


def solve(lines, n):
    min_line = 0
    max_line = n - 1
    ret = []

    while min_line <= max_line:
        top(min_line, lines, ret)
        right(lines, ret)
        max_line -= 1
        bottom(max_line, lines, ret)
        max_line -= 1
        left(min_line, max_line, lines, ret)

    print(*ret, sep=", ")


def main():
    if len(sys.argv) == 1:
        sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

    lines = sys.argv[1:]
    n = len(lines)

    validate(lines, n)
    solve(lines, n)


if __name__ == "__main__":
    main()  
