#!/usr/bin/python3

import sys

morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

if len(sys.argv) != 2:
	print("usage: ./osalmine.py <a-zA-Z string>")
	quit()

string = sys.argv[1].upper();
if len(string) == 0:
	print("usage: ./osalmine.py <a-zA-Z string>")
	quit()

if not all(x.isalpha() or x.isspace() for x in string):
	print("usage: ./osalmine.py <a-zA-Z string>")
	quit()

for letter in string:
	if (letter == " "):
		print(" ", end = '')
	else:
		print(morse[letter], end = '');
print()
