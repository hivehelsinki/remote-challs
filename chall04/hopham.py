#!/usr/bin/python3

n = int(input())

arr = []
for j in range(n):
    arr.append(list(input()))

for s in range(n - 1):
    for a, b in enumerate(arr[s]):
        if b == '.':
            if arr[s + 1][a] == ' ':
                arr[s][a] = ' '
                arr[s + 1][a] = '.'

for string in arr:
    for a in string:
        print(a, end="")
    print()
