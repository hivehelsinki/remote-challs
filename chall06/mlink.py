#!/usr/bin/env python3
import fileinput
import sys

def error(error_message, filename):
    print(f'{sys.argv[0]}: {filename}: {error_message}')

def solution(lines, filename):

    book = []
    bookshelfs = [int(i) for i in lines[0].split()]

    if len(bookshelfs) == 0:
        error("Can\'t read file", filename)
        return
    for i in range(1, len(lines)):
            lenght = int(lines[i].split()[0])
            book.append(lenght)

    book.sort(reverse=True)
    bookshelfs.sort(reverse=True)

    if book[0] > bookshelfs[0]:
        error('Not enough space in the given shelves', filename)
        return

    min_bookshelfs = -1
    a = len(bookshelfs)
    b = len(book)
    j = 0

    while j in range(b):
        i = 0
        flag = False
        while i in range(a):
            if bookshelfs[i] - book[j] >= 0:
                bookshelfs[i] = bookshelfs[i] - book[j]
                j += 1
                flag = True
                break
            else:
                i += 1
        if i > min_bookshelfs:
            min_bookshelfs = i
        if flag == False:
            error('Not enough space in the given shelves', filename)
            exit()

    print(min_bookshelfs + 1)

def main():
    argc = len(sys.argv)
    if argc == 2:
        filename = sys.argv[1]
        try:
            data = open(filename, 'r')
            solution(data.read().splitlines(), filename)
        except:
            error("Can't read file", filename)
    elif argc > 2:
        for i in range(1, argc):
            filename = sys.argv[i]
            print(f"{filename}:")
            try:
                data = open(filename, 'r')
                solution(data.read().splitlines(), filename)
            except:  
                error("Can't read file", filename)
            argc -= 1
            print()
    else:
        try:
            data = sys.stdin
            solution(data.read().splitlines(), 'stdin')
        except:
            error("Can't read file", 'stdin')

if __name__ == '__main__':
    main()