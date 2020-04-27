#!/usr/bin/env python3

import sys
import numpy as np


def print_outer(n):
    for i in range(n):
        path.append(array[0][i])
    for i in range(1, n):
        path.append(array[i][n-1])


n = len(sys.argv) - 1

if n < 1 or not all(arg.isdigit() and (len(arg) == n) for arg in sys.argv[1:]):
    sys.exit(f'usage: {sys.argv[0]} <1-9 squared_rows...>')

path = []
array = np.array([[int(n) for n in row] for row in sys.argv[1:]])

for i in range(n):
    print_outer(n - i)
    array = np.rot90(array[1:, :n-1-i], 2)

print(", ".join(str(n) for n in path))
