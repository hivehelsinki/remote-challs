#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print("usage: ./xlogin.py <a-zA-Z string>")
    sys.exit(1)


def to_morse_code(input):
    code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..'}
    morse_code = ""
    for x in input:
        if (x.isalpha() or x == ' '):
            if (x == ' '):
                morse_code += ' '
            else:
                morse_code += code[x.lower()]
        else:
            print("usage: ./xlogin.py <a-zA-Z string>")
            sys.exit(1)
    return morse_code


input = sys.argv[1]
if (input == ""):
    print("usage: ./xlogin.py <a-zA-Z string>")
    sys.exit(1)
print(to_morse_code(input))
