#!/usr/bin/env python3
import sys
import re

morse = {
	'a': '.-',
	'b': '-...',
	'c': '-.-.',
	'd': '-..',
	'e': '.',
	'f': '..-.',
	'g': '--.',
	'h': '....',
	'i': '..',
	'j': '.---',
	'k': '-.-',
	'l': '.-..',
	'm': '--',
	'n': '-.',
	'o': '---',
	'p': '.--.',
	'q': '--.-',
	'r': '.-.',
	's': '...',
	't': '-',
	'u': '..-',
	'v': '...-',
	'w': '.--',
	'x': '-..-',
	'y': '-.--',
	'z': '--..',
	' ': ' '
}

if (len(sys.argv) == 2):
	word = sys.argv[1].lower().strip()
	mode = 0
	for c in word:
		if c.isalpha() or c == ' ':
			mode = mode
		else:
			mode = 1
	if (mode == 0 and len(word) > 0):
		for char in word:
			sys.stdout.write(morse[char])
		print('')
	else:
		print("usage: ./spentti.py <a-zA-Z string>")
else:
	print("usage: ./spentti.py <a-zA-Z string>")