#!/usr/bin/env python3

import sys
from os import path
import errno

def parse_content(content):
    total = 0
    for i in content:
        if (i):
            width = i.split()[0]
            if (width.isdigit()):
                total += int(width)
            else:
                return -1 
    return total

def read_file(arg):
    try:
        f = open(arg, "r")
    except IOError as x:
        if x.errno == errno.ENOENT or x.errno == errno.EACCES:
            return (-1, -1)
    shelves = list((f.readline().split()))
    content = f.read().split('\n')
    total = parse_content(content)
    f.close()
    if total == -1: # non-number character in width 
        return (-1, -1)
    return shelves, total

def read_stdin():
    input = sys.stdin.read()
    content = input.split('\n')
    shelves = content[0].split()
    total = parse_content(content[1:])
    return shelves, total

def shelves(arg):
    if (arg == "stdin"):
        shelves, total = read_stdin()
    else:
        shelves, total = read_file(arg)
    if (shelves == -1 and total == -1):
        print(sys.argv[0] + ": " + arg + ": Can't read file")
        return
    
    shelves.sort(reverse=True)
    shelves_total = 0
    for i in range(len(shelves) - 1):
        if (shelves[i].isdigit()):
            shelves_total += int(shelves[i])
        if (total <= shelves_total):
            print(i + 1)
            return
    print(sys.argv[0] + ": " + arg + ": Not enough space in the given shelves")

def main():
    args = len(sys.argv) - 1
    if (args > 0): #read from file
        for arg in sys.argv[1:]:
            if (args > 1):
                print(arg + ":")
            shelves(arg)
    else: #read from command line
        shelves("stdin")

if __name__=="__main__":
    main()