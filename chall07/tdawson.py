#!/usr/bin/env python3

import sys
import numpy as np

rows = len(sys.argv) - 1

if rows not in range(1, 21) or not all(row.isdigit() and (len(row) == rows) for row in sys.argv[1:]):
    sys.exit(f'usage: {sys.argv[0]} <1-9 squared_rows...>')

array = np.array([list(row) for row in sys.argv[1:]])

path = []
for _ in range(rows):
    path.extend(list(n for n in array[0]))
    path.extend(list(n for n in array[1:, -1]))
    array = np.rot90(array[1:, :-1], 2)

print(", ".join(path))
