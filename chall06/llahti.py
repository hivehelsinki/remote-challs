#!/usr/bin/env python3
#Python 3.8.2
import sys
import os

def errorString(path, error):
    format = "{}: {}: {}"
    return format.format(sys.argv[0], path, error)

def startCount(shelves, collection):
    if shelves[0] < collection[0] or sum(collection) > sum(shelves):
        return -1
    count = 1
    shelveSum = shelves[0]
    while sum(collection) > shelveSum:
        shelveSum += shelves[count]
        count += 1
    return count

def fill(shelves, collection):
    if not collection:
        return True
    i = 0
    while i < len(shelves):
        if collection[0] < shelves[i]:
            shelves[i] -= collection[0]
            return fill(shelves, collection[1:])
        i += 1
    return False

def solve(path, shelves, collection):
    collection.sort(reverse=True)
    count = startCount(shelves, collection)
    if count == -1:
        return errorString(path, 'Not enough space in the given shelves')

    while not fill(shelves[:count], collection):
        count += 1
        if count > len(shelves):
            return errorString(path, 'Not enough space in the given shelves')    
    return count

def getShelves(line, stdin):
    strs = line.split()
    if stdin:
        strs.pop(0)
    
    shelves = []

    for s in strs:
        try:
            shelves.append(int(s))
        except ValueError:
            return None

    shelves.sort(reverse=True)
    return shelves

def readFile(path):
    with open(path) as fp:
        shelves = getShelves(fp.readline(), False)
        if not shelves:
            return errorString(path, "Can't read file")
        collection = []
        line = fp.readline()
        while line:
            try:
                collection.append(int(line.split().pop(0)))
            except ValueError:
                return errorString(path, "Can't read file")
            line = fp.readline()

    return solve(path, shelves, collection)

def readStdin():
    path = 'stdin'
    shelves = getShelves(sys.stdin.readline(), True)
    if not shelves:
        return errorString(path, "Can't read file")
    collection = []
    line = sys.stdin.readline()
    while line:
        try:
            collection.append(int(line.split().pop(1)))
        except ValueError:
            return errorString(path, "Can't read file")
        line = sys.stdin.readline()

    return solve(path, shelves, collection)

def main():
    args = len(sys.argv)

    if args < 2:
        if sys.stdin.isatty():
            print('Usage:\t./llahti.py <collectionfile.txt>\n   or:\t./llahti.py <collection as stdin>')
            return
        else:
            result = readStdin()
    else:
        arg = 1
        while arg < args:
            path = sys.argv[arg]

            if not os.path.isfile(path) or not os.access(path, os.R_OK):
                result = errorString(path, "Can't read file")
            else:
                result = readFile(path)

            if args > 2:
                resultFormat = '{}:\n{}\n'
                print(resultFormat.format(path, result))
            
            arg += 1
    
    if args < 3:
        print(result)

if __name__ == "__main__":
    main()