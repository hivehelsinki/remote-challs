#!/usr/bin/python3

import sys

def spiralPrint(m, n, a):

	k = 0
	l = 0
	arr = []
	while (k < m and l < n):
		# Get the first row from
		# the remaining rows
		for i in range(l, n):
			arr.append(a[k][i])

		k += 1
	
		# Get the last column from 
		# the remaining columns 
		for i in range(k, m):
			arr.append(a[i][n - 1])
		n -= 1

		# Get the last row from
		# the remaining rows
		if k < m:
			for i in range(n - 1, l - 1, -1):
				arr.append(a[m - 1][i])
			m -= 1
		
		# Get the first column from 
		# the remaining columns 
		if l < n:
			for i in range(m - 1, k - 1, -1):
				arr.append(a[i][l])
			l += 1

	for i in arr[:-1]:
		print(i, end= ", ")
	print(arr[-1])


if len(sys.argv) < 2:
	exit(f"usage: {sys.argv[0]} <1-9 squared_rows...>")
arr = sys.argv[1:]
arr_len = len(arr)
for i in arr:
	if len(i) != arr_len or not(i.isdigit()):
		exit(f"usage: {sys.argv[0]} <1-9 squared_rows...>")

spiralPrint(arr_len, arr_len, arr)

