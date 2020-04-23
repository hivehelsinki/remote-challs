#!/usr/bin/python3.7

import sys

def error(error_message, filename):
    print(f'{sys.argv[0]}: {filename}: {error_message}')

def get_collections_size(data):
    collections = []
    for i in range(1, len(data)):
        collection = data[i]
        collections.append(int(collection.split()[0]))
    return collections

def parse_and_solve(data, filename):
    shelves = [int(shelf) for shelf in data[0].split()]
    if len(shelves) == 0:
        exit()
    collections = get_collections_size(data)
    shelves.sort(reverse=True)
    unallocated_books_amount = sum(collections)
    if unallocated_books_amount == 0:
        print('0')
        return
    for i in range(len(shelves)):
        unallocated_books_amount -= shelves[i]
        if unallocated_books_amount <= 0:
            break
    if unallocated_books_amount > 0:
        error('Not enough space in the given shelves', filename)
    else:
        print(i + 1)

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

