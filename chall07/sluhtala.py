#!/usr/bin/python3
import sys

def put_usage():
    usage = "usage: ./sluhtala.py <1-9 squared_rows...>"
    print(usage)
    exit()

def print_sqr(nums, x, edge, new_nums):
    if edge == 1:
        new_nums.append(nums[x])
        return int(0)
    for i in range(edge):
        new_nums.append(nums[x])
        x += 1
    x -= 1
    for i in range(edge - 1):
        x += size
        new_nums.append(nums[x])
    for i in range(edge - 1):
        x -= 1
        new_nums.append(nums[x])
    edge -= 1
    for i in range(edge - 1):
        x -= size
        new_nums.append(nums[x])
    edge -= 1
    return int(edge)

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        put_usage
    args.pop(0)
    size = len(args)
    for i in range(size):
        if len(args[i]) != size:
            put_usage()
    nums = []
    for i in range(size):
        for j in range(size):
         if args[i][j].isnumeric() == 0:
              put_usage()
         nums.append(args[i][j])
    edge = size
    new_nums = []
    x = 0
    while edge > 0:
        edge = print_sqr(nums, x, edge, new_nums)
        x += size
        x += 1
    print(*new_nums, sep = ", ") 
