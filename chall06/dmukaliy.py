#!/usr/bin/python3.7

import sys

def error(error_message, filename):
    print(f'{sys.argv[0]}: {filename}: {error_message}')

def get_sorted_books_width(data):
    books = []
    for i in range(1, len(data)):
        book = data[i]
        books.append(int(book.split()[0]))
    books.sort(reverse=True)
    return books

def get_amount_shelves(shelves, books):
    shelves_amount = -1
    for i in range(0, len(books)):
        found = False
        for j in range(0, len(shelves)):
            if shelves[j] - books[i] >= 0:
                shelves[j] -= books[i]
                found = True
                break
        if j > shelves_amount:
            shelves_amount = j
        if not found:
            return -1
    return shelves_amount + 1

def parse_and_solve(data, filename):
    shelves = [int(shelf) for shelf in data[0].split()]
    if len(shelves) == 0:
        exit()
    books = get_sorted_books_width(data)
    if sum(books) == 0:
        print('0')
        return
    shelves.sort(reverse=True)
    if shelves[0] < books[0]:
        error('Not enough space in the given shelves', filename)
        return
    shelves_amount = get_amount_shelves(shelves, books)
    if shelves_amount == -1:
        error('Not enough space in the given shelves', filename)
    else:
        print(shelves_amount)

def main():
    argc = len(sys.argv)
    if argc > 1:
        for i in range(1, argc):
            filename = sys.argv[i]
            if argc > 2:
                print(f'{filename}:')
            try:
                input_file = open(filename, 'r')
                parse_and_solve(input_file.read().splitlines(), filename)
            except:
                error('Can\'t read file', filename)
            if i != argc - 1:
                print()
    else:
        try:
            input_file = sys.stdin
            parse_and_solve(input_file.read().splitlines(), 'stdin')
        except:
            error('Can\'t read file', 'stdin')

if __name__ == '__main__':
    main()

