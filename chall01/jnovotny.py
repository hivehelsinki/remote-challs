#!/usr/bin/python3
import sys

def usage_exit():
	print("usage: ./jnovotny.py <a-zA-Z string>")
	exit()

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
		elif letter in morse_dict.keys():
			str_out += f"{morse_dict[letter]}"
		else:
			usage_exit()
	return str_out



if __name__ == "__main__":
	if len(sys.argv) == 2 and len(sys.argv[1]) > 0:	
		print(morse(sys.argv[1].lower()))
	else:
		usage_exit()