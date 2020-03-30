#!/usr/bin/python3
import sys

def error():
	sys.stdout.write("usage: ./dmukaliy.py <a-zA-Z string>\n")
	exit()

def morse(string):
	alphabet = {" ":" ", "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....",
		"i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-",
		"r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
	for char in string:
		if char not in alphabet.keys():
			error()
	for char in string:
		sys.stdout.write(alphabet[char])
	sys.stdout.write("\n")

def main():
	if len(sys.argv) != 2 or not sys.argv[1]:
		error() 
	else:
		morse(sys.argv[1].lower())

if __name__ == "__main__":
	main()
