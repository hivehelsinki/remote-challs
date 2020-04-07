#!/usr/bin/python3

import sys

def main():
    default = [" ", ".", "#"]
    world = []
    try:
        size = int(input())
    except:
        print("Wrong number!")
        sys.exit()

    if size == 0:
        print("Wrong size!")
        sys.exit()
    
    for i in range(size):
        world.append(input())
        if len(world[i]) != size:
            print("Wrong length!")
            sys.exit()
        for j in world[i]:
            if not default.count(j):
                print("Wrong character!")
                sys.exit()
    
    for y in reversed(range(size - 1)):
        for x in range(size):
            for z in range(size - 1 - y):
                if world[y + z][x] == '.' and world[y + 1 + z][x] == ' ':
                    world[y + z] = world[y + z][:x] + ' ' + world[y + z][x + 1:]
                    world[y + 1 + z] = world[y + 1 + z][:x] + '.' + world[y + 1 + z][x + 1:]

    print("\n")
    for k in world:
        print(k)

if __name__ == "__main__":
    main()