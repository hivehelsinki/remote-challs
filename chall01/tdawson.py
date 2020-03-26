#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
	print("usage: ./xlogin.py <a-zA-Z string>")
	sys.exit()

string = sys.argv[1]

if not all(c.isalpha() or c.isspace() for c in string) or len(string) == 0:
	print("usage: ./xlogin.py <a-zA-Z string>")
	sys.exit()

string = string.lower()

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

for c in string:
	print(morse_alphabet[c], end="")
else:
	print("")