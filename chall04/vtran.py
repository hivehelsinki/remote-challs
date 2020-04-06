#!/usr/bin/python3

import re
import sys

siz = int(input())
arr = []
i = 0
while i < siz:
    arr.append(input())
    i += 1
i = siz - 1
while i >= 0:
    if (len(arr[i]) != siz) :
        print("input not a grid")
        sys.exit()
    i -= 1
listToStr = ''.join(map(str, arr))
maximum = str(siz * siz)
regex = "[. #]{" + maximum + "}"
if not re.match(regex, listToStr) :
    print("usage: [. #]*")
    sys.exit()
StrToList = list(listToStr)
i = 0
allcellsbutnotlastcolumns = siz * siz - siz
while (i < allcellsbutnotlastcolumns):
    if (StrToList[i] == '.' and StrToList[i + siz] == ' '):
        StrToList[i] = ' '
        StrToList[i + siz] = '.'
        i = 0
    i += 1
i = 0
while (i < siz):
    StrToList[i : i + siz] = [''.join(StrToList[i : i + siz])]
    print(StrToList[i])
    i += 1
