#!/usr/bin/python3.7

import sys

def check_validity(data):
    if not data or len(data) > 20:
        sys.exit(f'usage: {sys.argv[0]} <1-9 squared_rows...>')
    for row in data:
        if len(row) != len(data) or not row.isnumeric():
            sys.exit(f'usage: {sys.argv[0]} <1-9 squared_rows...>')

def solve(data):
    arr = [list(row) for row in data]
    result = []

    while arr:
        result.extend(arr.pop(0))
        for row in arr:
            result.extend(row.pop(len(row) - 1))
        for i in reversed(range(0, len(arr))):
            result.extend(arr[len(arr) - 1].pop(i))
        if arr: arr.pop()
        for i in reversed(range(0, len(arr))):
            result.extend(arr[i].pop(0))

    print(', '.join(result))

def main():
    data = sys.argv[1:]
    check_validity(data)
    solve(data)

if __name__ == '__main__':
    main()

