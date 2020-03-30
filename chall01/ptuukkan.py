#!/usr/bin/python3

import sys

codes = {
	"a": ".-",
	"b": "-...",
	"c": "-.-.",
	"d": "-..",
	"e": ".",
	"f": "..-.",
	"g": "--.",
	"h": "....",
	"i": "..",
	"j": ".---",
	"k": "-.-",
	"l": ".-..",
	"m": "--",
	"n": "-.",
	"o": "---",
	"p": ".--.",
	"q": "--.-",
	"r": ".-.",
	"s": "...",
	"t": "-",
	"u": "..-",
	"v": "...-",
	"w": ".--",
	"x": "-..-",
	"y": "-.--",
	"z": "--..",
	" ": " "
}

if (len(sys.argv) != 2 or (len(sys.argv[1]) == 0)):
	exit("usage: ./ptuukkan.py <a-zA-Z string>")

result = ""

for char in sys.argv[1]:
	if char.lower() in codes:
		result += codes[char.lower()]
	else:
		exit("usage: ./ptuukkan.py <a-zA-Z string>")
print(result)
