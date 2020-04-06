#!/usr/bin/python3

# Version: Python 3.6.9

def error_input(msg):
    print(msg)
    quit()

def can_move(next_under):
    if (next_under == ' '):
        return True
    return False

if __name__ == '__main__':
    size = input()
    if size.isdigit():
        size = int(size)
    else:
        error_input("Enter a positive number")

    grid = [list(input()) for i in range(size)] # Split 'size' amount of lines into lists of characters

    # Check that every line in grid is of the correct length
    for row in grid:
        if (len(row) != size):
            error_input("Length of each line must be same as size")

    moved = True
    # Loop ends when no sand has been moved
    while moved:
        moved = False
        for row in range(size):
            for col in range(size):
                if (row + 1 < size and grid[row][col] == '.'):
                    if (can_move(grid[row + 1][col])):
                        grid[row][col] = ' '
                        grid[row + 1][col] = '.'
                        moved = True

    for row in grid:
        output_str = ''.join(i for i in row)
        print(output_str)
