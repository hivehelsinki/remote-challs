#!/usr/bin/python3

import sys

class Error(Exception):
    pass

class ValidationError(Error):

    def __init__(self, message):
        self.message = message


def format_rows(rows: list): 
    r = []
    for row in rows:
        r.append([c for c in row])
    return r


def validate():
    rows = []
    sys.argv.pop(0)
    for arg in sys.argv:
        rows.append(arg)

    if not len(rows):
        raise ValidationError('No input')
    if not all(len(row) == len(rows[0]) for row in rows):
        raise ValidationError('Invalid line lenght')
    if not len(rows[0]) == len(rows):
        raise ValidationError('Input not a square')

    return rows



def snail(rows: list):
    result = []
    slots = len(rows) * len(rows)
    rows = format_rows(rows)
    start_y = 0
    start_x = 0
    end_y = len(rows) - 1
    end_x = len(rows[0]) - 1
    while slots:
        i = start_x
        while i <= end_x:
            result.append(rows[start_y][i])
            i += 1
            slots -= 1
        start_y += 1

        i = start_y
        while i <= end_y:
            result.append(rows[i][end_x])
            i += 1
            slots -= 1
        end_x -= 1
        
        i = end_x
        while i >= start_x:
            result.append(rows[end_y][i])
            i -= 1
            slots -= 1
        end_y -= 1

        i = end_y
        while i >= start_y:
            result.append(rows[i][start_x])
            i -= 1
            slots -= 1
        start_x += 1

    return result


def main():
    try:
        rows = validate()
        r = snail(rows)
        print(', '.join(r))
    except Exception as e:
        print(f'Something went wrong: {e}')


if __name__ == '__main__':
    main()