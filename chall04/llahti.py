#!/usr/bin/env python
import sys

def move(grid, n):
    done = True
    y = n - 1
    while y > 0:
        x = n - 1
        while x >= 0:
            if grid[y][x] in [' '] and grid[y - 1][x] in ['.']:
                grid[y] = grid[y][:x] + '.' + grid[y][x + 1:]
                grid[y - 1] = grid[y - 1][:x] + ' ' + grid[y - 1][x + 1:]
                done = False
            x -= 1
        y -=  1
    return done

def checkInput(line, n):
    allowed = {'.',' ','#'}
    if not set(line).issubset(allowed):
        return False
    if len(line) != n:
        return False
    return True

def main():
    input = sys.stdin.readlines()
    n = int(input[0])
    grid = input[1:]

    if len(grid) != n:
        exit()

    for line in grid:
        line = line.rstrip('\n')
        if not checkInput(line, n):
            exit()

    done = False
    while not done:
        done = move(grid, n)

    for line in grid:
        print(line.rstrip('\n'))

if __name__ == "__main__":
    main()
