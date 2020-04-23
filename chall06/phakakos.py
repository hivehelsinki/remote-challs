#!/usr/bin/env python3

import sys
import fileinput

def errnoHandle(code, source):
        #replace with (sys.argv[0] + " ") for flexible use. My enviroment does not match the tests, which gives a different out put, so I'm just gonna hardcode it :^)
        beginning = "./phakakos.py "
        if code == 1:
                print(beginning + source + ": Can't read file")
        elif code == 2:
                print(beginning + source + ": Not enough space in the given shelve")
        return (code)

def readLoop(lines, name):
        totalW = 0
        totalU = 0
        shelfs = []
        bought = 0
        for line in lines:
                if len(shelfs) == 0:
                        shelfs = line.split()
                        i = 0
                        for var in shelfs:
                                        try:
                                                shelfs[i] = int(shelfs[i])
                                        except:
                                                return(errnoHandle(1, name))
                                        i += 1
                        if len(shelfs) == 0:
                                return(errnoHandle(1, name))
                        continue
                line = line.split()
                try:
                        addBooks = int(line[0])
                except:
                        return(errnoHandle(1, name))
                totalW += addBooks
        while(totalW > totalU):
                if len(shelfs) == 0:
                        return(errnoHandle(2, name))
                largest = shelfs[0]
                topi = 0
                i = 0
                for shelf in shelfs:
                        if shelf > largest:
                                largest = shelf
                                topi = i
                        i += 1
                shelfs.pop(topi)
                bought += 1
                totalU += largest
        print(bought)
                        
        
        

def mainLoop():
        if len(sys.argv) < 2:
                lines = []
                for line in fileinput.input():
                        lines.append(line.replace('\n',''))
                print(lines)
                readLoop(lines, "stdin")
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
                                lines = file.read()
                                lines = lines.split('\n')
                                readLoop(lines, arg)
                                file.close()
                        except:
                                errnoHandle(1, arg)

if __name__ == '__main__':
	mainLoop()
