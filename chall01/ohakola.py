#!/usr/bin/env python3
import sys

usage = "usage: ./ohakola.py <a-zA-Z string>"
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

def print_args():
	args_len = len(sys.argv)
	str = sys.argv[1].lower()
	if (args_len == 2):
		str_len = len(str)
		if (str_len == 0):
			print(usage)
			return
		i = 0
		while (i < str_len):
			char = str[i]
			if (i < str_len - 1):
				print(morse_dict[char], end = '')
			else:
				print(morse_dict[char], end = '\n')
			i += 1
	else:
		print(usage)

print_args()
