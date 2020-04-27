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
    str1 = arrToStr(arr)
    maximum = str(siz * siz)
    regex = "[. #]{" + maximum + "}"
    if not re.match(regex, str1) :
        print("usage: [. #]*")
        sys.exit()

def arrToStr(arr):
    return ''.join(map(str, arr))

def droppingDots(str1, siz):
    arr = list(str1)
    i = 0
    allcellsbutnotlastcolumns = siz * siz - siz
    while (i < allcellsbutnotlastcolumns):
        if (arr[i] == '.' and arr[i + siz] == ' '):
            arr[i] = ' '
            arr[i + siz] = '.'
            i = 0
        i += 1
    return arr

def printter(arr, siz):
    i = 0
    while (i < siz):
        arr[i : i + siz] = [''.join(arr[i : i + siz])]
        print(arr[i])
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