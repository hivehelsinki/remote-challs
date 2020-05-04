#!/usr/bin/env python3

import sys
import itertools

if __name__ == "__main__":
    array = []
    args = len(sys.argv) - 1
    if (args == 0):
        print(f"usage: {sys.argv[0]} <1-9 squared_rows...>")
        exit()
    else:
        
        square_side_length = args
        for arg in sys.argv[1:]:
            if (len(arg) != square_side_length):
                print(f"usage: {sys.argv[0]} <1-9 squared_rows...>")
                exit()
            if (arg.isdigit()):
                array.append(list(arg))
            else:
                print(f"usage: {sys.argv[0]} <1-9 squared_rows...>")
                exit()

    snail = []
    while (array):
        if (array):
            first = array.pop(0)
            snail.append(first)
        if (array):
            second = []
            for i in array:
                second.append(i.pop())
            snail.append(second)
        if (array):
            third = array.pop()
            third.reverse()
            snail.append(third)
        if (array):
            fourth = []
            for i in reversed(array):
                fourth.append(i.pop(0))
            snail.append(fourth)
    
    out = list(itertools.chain.from_iterable(snail))
    print(", ".join(out))
