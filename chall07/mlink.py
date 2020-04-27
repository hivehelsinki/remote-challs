#!/usr/bin/env python3
import sys

rows = len(sys.argv) - 1
array = []
newarray = []

if 1 <= rows <= 20:

    for i in range(1, rows + 1):
        if len(sys.argv[i]) == rows:
            s = sys.argv[i]
            for j in range(rows):
                if s[j] > '9' or s[j] < '0':
                    print(f"usage: {sys.argv[0]} <1-9 squared_rows...>")
                    exit() 
            array.append(list(sys.argv[i]))
        else:
            print(f"usage: {sys.argv[0]} <1-9 squared_rows...>")
            exit()

    while rows > 0:

        if rows > 0:
            step = array.pop(0)
            newarray.extend(step)
            rows -= 1

        if rows > 0:
            for i in range(rows):
                step = array[i].pop()
                newarray.append(step)
            step = array.pop()
            step.reverse()
            newarray.extend(step)
            rows -= 1

        if rows > 1:
            for i in range(rows - 1, 0, -1):
                step = array[i].pop(0)
                newarray.extend(step)

    print(', '.join(newarray))

else:
    print(f"usage: {sys.argv[0]} <1-9 squared_rows...>")