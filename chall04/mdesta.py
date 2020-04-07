#!/usr/bin/env python3
# Python3 Falling Sand Stone

# To Reverse the string
def revString(str):
  return str[::-1]

# PrintOut Error and Exit
def printError():
    print("Input Error")
    exit()

# Print final OutPut
def printOutput():
    i = 0
    j = 0
    while j < gridSize:
        k = 0
        while k < gridSize and i < len(finalString):
            print(finalString[i], end ="")
            i += 1
            k += 1
        print()
        j += 1

# Solves One Column Starting From given Column
# Every nth (n = gridSize) element makes a column
# Recurssively Swap elements if current is empty
# and next is sand
def solveColumn(rawString, kol):
    i = kol
    while i <= (len(rawString) - (2 * gridSize) + kol):    
        if rawString[i] == ' ' and rawString[i + gridSize] == '.':
            temp = rawString[i]
            rawString[i] = rawString[i + gridSize]
            rawString[i + gridSize] = temp
            solveColumn(rawString, kol)
        else:
            i += gridSize
    return rawString

# Program Starts Here
# Get grid size 
gridSize = int(input())

# Get the Input
# Read n = GridSize lines
# Check if line size is valid
# and contains only valid characters
inputString = ''
i = 0
while i < gridSize:
    line = str(input())
    if len(line) != gridSize:
        printError()
    for char in line:
        if char not in " .#":
            printError()
    inputString += line
    i += 1

# Reverse String and Convert it to List
# for Easy Manipulation
rawString = list(revString(inputString))

# Solve For Every Column
kol = 0
while kol < gridSize:
    rawString = solveColumn(rawString, kol)
    kol += 1

# Convert back List to String and 
# reverse it to get the final result
finalString = revString(''.join(rawString))

# Printing The Final OutPut
printOutput()
