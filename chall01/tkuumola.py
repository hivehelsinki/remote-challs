#!/usr/bin/env python3

import sys

morse_code = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    ' ':' ',
}

if len(sys.argv) != 2:
    print ('usage: ./tkuumola.py <a-zA-Z string>')
    sys.exit(1)

input = sys.argv[1].upper()
len = len(" ".join(input.split()))

if all(x in morse_code for x in input) and len != 0:
    for elem in input:
            print(morse_code[elem], end = '')
    print()
else:
    print ('usage: ./tkuumola.py <a-zA-Z string>')