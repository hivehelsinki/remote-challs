#!/usr/bin/python3

import sys

def make_snail(array, start, end):
	[snail.append(i) for i in array[start][start:end:1]]
	[snail.append(sub[end]) for sub in array[start:end:1]]
	[snail.append(i) for i in array[end][end:start:-1]]
	[snail.append(sub[start]) for sub in array[end:start:-1]]
	if (start + 1 == end - 1):
		snail.append(array[start + 1][end - 1])
	if (start + 1 < end - 1):
		make_snail(array, start + 1, end - 1)

for row in sys.argv[1::]:
	if len(sys.argv[1::]) != len(row) or not row.isnumeric():
		sys.exit(f'usage: {sys.argv[0]} <1-9 squared_rows...>')

snail = []
make_snail(sys.argv[1::], 0, len(sys.argv[1::]) - 1)
print (', '.join(snail))
