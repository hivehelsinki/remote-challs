#!/usr/bin/python3
import sys

if len(sys.argv) != 2 or not isinstance(sys.argv[1], str) or len(sys.argv[1]) == 0:
	print("usage: ./xlogin.py <a-zA-Z string>")
	sys.exit()

morse_alphabet = {
	"a" : ".-",
	"b" : "-...",
	"c" : "-.-.",
	"d" : "-..",
	"e" : ".",
	"f" : "..-.",
	"g" : "--.",
	"h" : "....",
	"i" : "..",
	"j" : ".---",
	"k" : "-.-",
	"l" : ".-..",
	"m" : "--",
	"n" : "-.",
	"o" : "---",
	"p" : ".--.",
	"q" : "--.-",
	"r" : ".-.",
	"s" : "...",
	"t" : "-",
	"u" : "..-",
	"v" : "...-",
	"w" : ".--",
	"x" : "-..-",
	"y" : "-.--",
	"z" : "--..",
	" " : " "
}

string = sys.argv[1].lower()

if not all(c in morse_alphabet for c in string):
	print("usage: ./xlogin.py <a-zA-Z string>")
	sys.exit()

for c in string:
	print(morse_alphabet[c], end="")
else:
	print("")