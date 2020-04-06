# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ohakola.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ohakola <ohakola@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/06 17:30:11 by ohakola           #+#    #+#              #
#    Updated: 2020/04/06 17:32:21 by ohakola          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3
import sys

# Swaps two characters in a string and returns a new string
def char_swap(str_in, at, at2):
	arr = list(str_in)
	arr[at], arr[at2] = arr[at2], arr[at]
	''.join(arr)
	return ''.join(arr)

# Simulates sand fall of given string (grid) and given row size
# each sand piece falls as long as there's empty below it
def sand_fall(grid, row_size):
	for y in range(row_size):
		for x in range(row_size):
			if y < 4:
				curr_index = y * row_size + x
				nxt_index = curr_index + row_size
				if grid[curr_index] == "." and grid[nxt_index] == " ":
					grid = char_swap(grid, curr_index, nxt_index)
	return grid

# prints grid string of given size
def print_grid(grid, size):
	for y in range(size):
		for x in range(size):
			print(grid[y * size + x], end = "")
		print("\n", end = "")

if __name__ == "__main__":
	lines = sys.stdin.readlines()
	row_size = int(lines.pop(0))
	for index, line in enumerate(lines) :
  		lines[index] = line.rstrip("\n")
	initial_grid = str.join("", lines)
	simulated_grid = sand_fall(initial_grid, row_size)
	print_grid(simulated_grid, row_size)
