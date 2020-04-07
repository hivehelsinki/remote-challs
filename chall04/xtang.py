#!/usr/bin/python3

import sys

def main():
    default = [" ", ".", "#"]
    world = []
# get integer from standard input
    try:
        size = int(input())
    except:
        print("Wrong number!")
        sys.exit()
# verify the value of integer
    if size == 0:
        print("Wrong size!")
        sys.exit()
# get input characters from standard input and verify the length and letters.    
    for i in range(size):
        world.append(input())
        if len(world[i]) != size:
            print("Wrong length!")
            sys.exit()
        for j in world[i]:
            if not default.count(j):
                print("Wrong character!")
                sys.exit()
# compare two characters located at uppper postion and lower postion in the same column     
    for y in reversed(range(size - 1)):
        for x in range(size):
            for z in range(size - 1 - y):
                if world[y + z][x] == '.' and world[y + 1 + z][x] == ' ':
                    world[y + z] = world[y + z][:x] + ' ' + world[y + z][x + 1:]
                    world[y + 1 + z] = world[y + 1 + z][:x] + '.' + world[y + 1 + z][x + 1:]
# print out the result
    print("\n")
    for k in world:
        print(k)

if __name__ == "__main__":
    main()
