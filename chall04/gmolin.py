#!/usr/bin/python3

import sys

def main():
	board = []
	for line in sys.stdin:
		board.append(list(line))
	board_size = int
	for i in board[0]:
		if i.isdigit():
			board_size = int(i)
	if board_size != len(board) - 1:
		print("Error: Invalid map size")
		return
	else:
		i = 1
		while (i < board_size):
			j = 0
			if (len(board[i]) - 1 != board_size):
				print ("Error: Invalid line length")
				return
			while (j < board_size):
				if (board[i][j] != "." and board[i][j] != "#" and board[i][j] != ' '):
					print("Error: Invalid map pieces")
					return
				try:
					if (board[i][j] == "." and board[i + 1][j] == " "):
						board[i + 1][j] = "."
						board[i][j] = " "
				except:
					print("Error: Invalid file")
					return
				j += 1
			i += 1
		i = 1
		while (i <= board_size):
			print(board[i])
			i += 1
if __name__ == "__main__":
	main()
