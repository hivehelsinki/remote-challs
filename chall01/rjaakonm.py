#!/usr/bin/python3

import sys

morse = [".-",
	"-...",
	"-.-.",
	"-..",
	".",
	"..-.",
	"--.",
	"....",
	"..",
	".---",
	"-.-",
	".-..",
	"--",
	"-.",
	"---",
	".--.",
	"--.-",
	".-.",
	"...",
	"-",
	"..-",
	"...-",
	".--",
	"-..-",
	"-.--",
	"--.."]

def main():
	if (len(sys.argv) != 2) or (len(sys.argv[1]) == 0):
		print("usage: ./rjaakonm.py <a-zA-Z string>")
		return
	str = ""
	sys.argv[1] = sys.argv[1].lower()
	for char in sys.argv[1]:
		if char.isalpha():
			str += morse[ord(char) - 97]
		elif char == " ":
			str += " "
		else:
			print("usage: ./rjaakonm.py <a-zA-Z string>")
			return
	print(str)

if __name__ == "__main__":
	main() 