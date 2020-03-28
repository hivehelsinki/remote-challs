#!/usr/bin/python3

import sys

MAPPING = {
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

def print_usage():
	print('usage: ./srouhe.py <a-zA-Z string>')
	sys.exit(1)

def encode_arg(s):
	r = ''
	for c in s:
		try:
			r += MAPPING[c]
		except KeyError:
			print_usage()
	return r

def main():
	if len(sys.argv) != 2:
		print_usage()
	if len(sys.argv[1]) == 0:
		print_usage()
	morse = encode_arg(sys.argv[1].lower())
	print(morse)

if __name__ == '__main__':
	main()
