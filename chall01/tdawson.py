#!/usr/bin/python3
import sys

def error():
    print(f'usage: {sys.argv[0]} <a-zA-Z string>')
    sys.exit()

if len(sys.argv) != 2 or not isinstance(sys.argv[1], str) or len(sys.argv[1]) == 0:
    error()

morse_alphabet = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                  'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
                  'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                  'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
                  'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ': ' '}

string = sys.argv[1].lower()

if not all(c in morse_alphabet for c in string):
    error()

for c in string:
    print(morse_alphabet[c], end='')
else:
    print('')
