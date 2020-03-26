#!/usr/bin/python3
import sys

def morse(string):
	morse_dict = {
		"a":".-",
		"b":"-...",
		"c":"-.-.", 
		"d":"-..",
		"e":".",
		"f":"..-.", 
		"g":"--.",
		"h":"....",
		"i":"..",
		"j":".---",
		"k":"-.-",
		"l":".-..",
		"m":"--",
		"n":"-.",
		"o":"---",
		"p":".--.",
		"q":"--.-",
		"r":".-.",
		"s":"...",
		"t":"-",
		"u":"..-",
		"v":"...-",
		"w":".--",
		"x":"-..-",
		"y":"-.--",
		"z":"--.."}
	str_out = ""
	for letter in string:
		if letter == " ":
			str_out += " "
		else:
			str_out += f"{morse_dict[letter]}"
	return str_out

if __name__ == "__main__":
	if len(sys.argv) == 2:
		for word in  sys.argv[1].split():
			if not word.isalpha():
				print("usage: ./jnovotny.py <a-zA-Z string>")
				exit()
		print(morse(sys.argv[1].lower()))
	else:
		print("usage: ./jnovotny.py <a-zA-Z string>")