#!/usr/bin/python3

import sys

def errorMessage():
	print(f"usage: {sys.argv[0]} <a-zA-Z string>")
	exit()

morse_dict = {
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
"z": "--.."
}

def check_chars(word, morse_dict):
	for x in word:
		if x.isalpha() == False:
			if x.isspace() == False:
				errorMessage()
		else:
			if x not in morse_dict:
				errorMessage()

if (len(sys.argv)) != 2 or not sys.argv[1]:
	errorMessage()
else:
	word = sys.argv[1].lower()
	check_chars(word, morse_dict)
	for x in word:
		if (x.isalpha()):
			print(morse_dict[x], end='')
		elif (x.isspace()):
			print(" ", end='')
		else:
			errorMessage()
print()
