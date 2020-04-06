#!/usr/bin/python3
#python 3.6.9

import re
import sys

def exitIfNotValidInput(siz, arr):
    i = siz - 1
    while i >= 0:
        if (len(arr[i]) != siz) :
            print("input not a grid")
            sys.exit()
        i -= 1
    listToStr = arrToStr(arr)
    maximum = str(siz * siz)
    regex = "[. #]{" + maximum + "}"
    if not re.match(regex, listToStr) :
        print("usage: [. #]*")
        sys.exit()

def arrToStr(arr):
    return ''.join(map(str, arr))

def droppingDots(listToStr, siz):
    StrToArr = list(listToStr)
    i = 0
    allcellsbutnotlastcolumns = siz * siz - siz
    while (i < allcellsbutnotlastcolumns):
        if (StrToArr[i] == '.' and StrToArr[i + siz] == ' '):
            StrToArr[i] = ' '
            StrToArr[i + siz] = '.'
            i = 0
        i += 1
    return StrToArr

def printter(StrToArr, siz):
    i = 0
    while (i < siz):
        StrToArr[i : i + siz] = [''.join(StrToArr[i : i + siz])]
        print(StrToArr[i])
        i += 1

def main ():
    siz = int(input())
    arr = []
    i = 0
    while i < siz:
        arr.append(input())
        i += 1
    exitIfNotValidInput(siz, arr)
    done = droppingDots(arrToStr(arr), siz)
    printter(done, siz)
main()