#!/usr/bin/python3

import sys
import string

def get_shelf(shelves, books):
    i = 0
    while i < len(shelves) :
        if len(books) == 0:
            return (i)
        for b in books:
            if b <= shelves[i]:
                shelves[i] -= b
                books.remove(b)
                if len(books) == 0:
                    break
                if shelves[i] != 0:
                    i = -1
                break
        i += 1
    return 0        

def bookshelf(input, count):
    for i in input:

        try:
            file = open(i)

            lines = file.readlines()
            line1 = lines.pop(0)
            shelves = line1.split()
            for s in shelves:
                if s.isdigit() is False:
                    print("%s: %s: Can't read file"% (sys.argv[0], i))
                    return
            shelves = list(map(int, shelves))
            shelves.sort(reverse=True)
            books = []
            for line in lines:
                strings = line.split()
                if strings[0].isdigit():
                    books.append(int(strings[0]))
                else:
                    print("%s: %s: Can't read file"% (sys.argv[0], i))
                    return
            books.sort(reverse=True)
            if count > 1:
                print("%s:"% i)
            nb = get_shelf(shelves, books)
            if nb != 0:
                print(nb)
            else:
                print("%s: %s: Not enough space in the given shelves"% (sys.argv[0],i))
            if i is not input[-1]:
                print()
        except IOError:
            print("%s: %s: Can't read file"% (sys.argv[0], i))


if len(sys.argv) > 1:
    arguments = sys.argv[1:]
    bookshelf(arguments, len(arguments))
elif sys.stdin != None:
    file = open("stdin", "a")
    for line in sys.stdin:
        file.write(line)
    file.close()
    arr = ["stdin"]
    bookshelf(arr, 1)
