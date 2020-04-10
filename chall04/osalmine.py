#!/usr/bin/python3

# Python 3.8.2

import sys
import fileinput

def append_space(list, size):
    for i, s in enumerate(list):
        if len(s) == 0:
            list[i] = "     "
        elif len(s) < size:
            amount = size - len(s)
            for _ in range(amount):
                s += ' '
            list[i] = s
        elif len(s) > size:
            raise Exception("line '{0}' shouldn't have more then {1} characters".format(s, size))
    return list

def replace_sand(list, i, j, size):
    ind = len(list) - i - 1
    for k, search in enumerate(list[ind:]):
        if ind + k is size or list[ind + k + 1][j] is not ' ':
            tmp = list[ind][:j] + ' ' + list[ind][j + 1:]
            list[ind] = tmp
            tmp = list[ind + k][:j] + '.' + list[ind + k][j + 1:]
            list[ind + k] = tmp
            return list

def main():
    inp = []
    for line in fileinput.input():
        inp.append(line)
    list = [x[:-1] for x in inp]
    for str in list[1:]:
        for char in str:
            if char != ' ' and char != '#' and char != '.':
                raise Exception("input can only contain ' ', '#' and '.'")
    if not list[0].isdigit():
        raise Exception("size can't be other than digits")
    size = int(list[0])
    append_space(list, size)
    list.reverse()
    for i, line in enumerate(list):
        if i is size or i is 0:
            continue
        for j, char in enumerate(line):
            if char is '.':
                list.reverse()
                list = replace_sand(list, i, j, size)
                list.reverse()
    list.reverse()
    print("\n")
    for line in list[1:]:
        print(line)

if __name__ == '__main__':
    main()
