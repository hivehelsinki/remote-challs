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
input = " ".join(input.split())

if all(x.isalpha() or x.isspace() for x in input) and len(input) != 0:
    for elem in input:
        if elem in morse_code:
            print(morse_code[elem], end = '')
    print()
else:
    print ('usage: ./tkuumola.py <a-zA-Z string>')