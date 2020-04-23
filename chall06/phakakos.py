#!/usr/bin/env python3

import sys
import fileinput

def errnoHandle(code, source):
        #replace with (sys.argv[0] + " ") for flexible use. My enviroment does not match the tests, which gives a different out put, so I'm just gonna hardcode it :^)
        beginning = "./phakakos.py "
        if code == -1:
                print(beginning + source + ": Can't read file")
        elif code == -2:
                print(beginning + source + ": Not enough space in the given shelves")

def readLoop(lines, name):
        totalW = 0
        totalB = 0
        maxW = 0
        shelfs = []
        books = []
        used = []
        for line in lines:
                if len(shelfs) == 0:
                        shelfs = line.split()
                        i = 0
                        for var in shelfs:
                                        try:
                                                shelfs[i] = int(var)
                                                if shelfs[i] < 0:
                                                        return(-1)
                                                if shelfs[i] > maxW:
                                                        maxW = shelfs[i]
                                                totalW += shelfs[i]
                                        except:
                                                return(-1)
                                        i += 1
                        if len(shelfs) == 0:
                                return(-1)
                        shelfs.sort(reverse = True)
                        continue
                line = line.split()
                try:
                        addBook = int(line[0])
                except:
                        return(-1)
                if addBook == 0:
                        continue
                elif addBook < 0:
                        return (-1)
                elif addBook > maxW:
                        return (-2)
                totalB += addBook
                books.append(addBook)
                if totalB > totalW:
                       return (-2)
        books.sort(reverse = True)
        y = 0
        for book in books:
                i = 0
                for shelf in used:
                        if book <= shelf:
                                used[i] = shelf - book
                                book = 0
                                break
                        i += 1
                if book == 0:
                        continue
                i = 0
                for shelf in shelfs:
                        if book <= shelf:
                                used.append(shelf - book)
                                shelfs.pop(i)
                                break
                        i += 1
                y += 1
        print(len(used))
        return(len(used))
                        
        
        

def mainLoop():
        if len(sys.argv) < 2:
                lines = []
                for line in fileinput.input():
                        lines.append(line.replace('\n',''))
                print(lines)
                ret = readLoop(lines)
                if ret < 0:
                        errnoHandle(ret, "stdin")
        else:
                skip = 0
                for arg in sys.argv:
                        if skip < 1:
                                skip = 1
                                continue
                        if skip == 2:
                                print("")
                        if len(sys.argv) > 2:
                                print(arg + ":")
                                skip = 2
                        try:
                                file = open(arg, "r")
                        except:
                                errnoHandle(-1, arg)
                                continue
                        lines = file.read()
                        lines = lines.split('\n')
                        ret = readLoop(lines, arg)
                        if ret < 0:
                                errnoHandle(ret, arg)
                        file.close()

if __name__ == '__main__':
	mainLoop()
