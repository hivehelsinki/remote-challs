#!/usr/bin/python3

# Version: python3.7

import sys
import re
import hashlib

def calculateHashOfArray(array):
	arrayStr = ''
	for row in array:
		arrayStr += row
	return hashlib.md5(arrayStr.encode('utf-8')).hexdigest()

try:
	size = int(input())
except:
	print('Give the size of the board as an integer')
	sys.exit()
board = []
if size == 0:
	sys.exit()
for i in range(size):
	board.append(input())

for row in board:
	if not re.match('^[ \.#]+$', row):
		print('Enter only valid characters (" ", ".", "#")')
		sys.exit()
	if len(row) != size:
		print('Enter a complete row')
		sys.exit()

oldChecksum = calculateHashOfArray(board)
while True:
	for rowIndex in range(len(board) - 2, -1, -1):
		row = board[rowIndex]
		for i in range(size):
			if row[i] == '.':
				if board[rowIndex + 1][i] == ' ':
					nextRow = board[rowIndex + 1]
					nextRow = nextRow[:i] + '.' + nextRow[i + 1:]
					board[rowIndex + 1] = nextRow
					board[rowIndex] = board[rowIndex][:i] + ' ' + board[rowIndex][i + 1:]
	checksum = calculateHashOfArray(board)
	if checksum == oldChecksum:
		break
	oldChecksum = checksum

for row in board:
	print(row)
