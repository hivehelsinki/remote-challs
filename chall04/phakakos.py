#!/usr/bin/env python3

import sys
import fileinput

def err(num):
        if (num == 0):
                print("Give size as a number")
                exit(1)
        if (num == 1):
                print("Invalid map input. Please check")
                exit(2)
        if (num == 2):
                print("Map width does not match")
                exit(3)

def allowedChar(c):
        allowed ={
                "." : ".",
                "#" : "#",
                " " : " ",
                "\n" : "\n"
                }
        return allowed.get(c, "error")

def lineCount(line, size):
        i = 0
        for c in line:
                if (allowedChar(c) == "error"):
                        err(1)
                if (c == '\n'):
                        if (i != size):
                                err(2)
                        i = 0
                else:
                        i += 1
        return line.count('\n')

def moveSand(map, size):
        ret = list(map)
        i = (size + 1) * size - 2
        while i > size:
                if (ret[i] == ' '):
                        y = i - size - 1
                        while y >= 0:
                                if (ret[y] == '.'):
                                        ret[y] = ' '
                                        ret[i] = '.'
                                        break
                                if (ret[y] == '#'):
                                        break
                                y = y - size - 1
                i -= 1 
        print("".join(ret))

def mainLoop():
        size = -1
        lines = 0
        map = ""
        for line in fileinput.input():
                if (size == -1):
                        try:
                                size = int(line)
                        except:
                                err(0)
                        if (size == 0):
                                exit()
                        continue
                map += line
                lines += lineCount(line, size)
                if (lines == size):
                        break
        moveSand(map, size)


if __name__ == '__main__':
	mainLoop()
