# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ohakola.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ohakola <ohakola@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/06 17:30:11 by ohakola           #+#    #+#              #
#    Updated: 2020/04/06 17:47:59 by ohakola          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3
import sys

# Simulates sand fall of given grid array where
# each sand piece falls as long as there's empty below it
def sand_fall(grid, row_size):
	for y in range(row_size):
		for x in range(row_size):
			if y < 4:
				curr_i = y * row_size + x
				nxt_i = curr_i + row_size
				if grid[curr_i] == "." and grid[nxt_i] == " ":
					grid[curr_i], grid[nxt_i] = grid[nxt_i], grid[curr_i]
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
	initial_grid = list("".join(lines))
	simulated_grid = sand_fall(initial_grid, row_size)
	print_grid(simulated_grid, row_size)
