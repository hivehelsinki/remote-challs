#!/usr/bin/python3
import sys

def main():
	nums = sys.argv
	length = len(nums) - 1
	dist_edge = 1
	x = 0
	y = 0

	del(nums[0])
	for arg in nums:
		for char in arg:
			if (char < '0' or char > '9'):
				print("usage: " + sys.argv[0] + " <1-9 squared_rows...>")
				return
		if (len(arg) != length):
			print("usage: " + sys.argv[0] + " <1-9 squared_rows...>")
			return
	while (dist_edge <= length / 2 + 1):
		y = dist_edge - 1
		x = y
		while (x < length - dist_edge):
			print(str(nums[y][x]) + ", ", end="")
			x += 1
		while (y < length - dist_edge):
			print(str(nums[y][x]) + ", ", end="")
			y += 1
		while (x >= dist_edge):
			print(str(nums[y][x]) + ", ", end="")
			x -= 1
		while (y >= dist_edge):
			print(str(nums[y][x]) + ", ", end="")
			y -= 1
		dist_edge += 1
	if (length % 2):
		tmp = int(length / 2)
		print(nums[tmp][tmp], end="")
	print("")

if __name__ == "__main__":
	main()
