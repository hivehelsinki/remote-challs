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

string = sys.argv[1].upper()
str_len = len(" ".join(string.split()))

if all(x in morse_code for x in string) and str_len != 0:
    for elem in string:
            print(morse_code[elem], end = '')
    print()
else:
    print ('usage: ./tkuumola.py <a-zA-Z string>')