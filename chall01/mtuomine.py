#!/usr/bin/env python3

import sys
import re

MORSES = {
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
'Z':'--..'
}

def encrypt(msg):
	msg = msg.upper()
	morse = ''
	for c in msg:
		if c == ' ':
			morse += ' '
		else:
			morse += MORSES[c]
	return morse

p = re.compile('[A-Za-z ]+$')

if len(sys.argv) != 2 or not p.match(sys.argv[1]):
	print("usage: ./mtuomine.py <a-zA-Z string>")
	exit()

print(encrypt(sys.argv[1]))
