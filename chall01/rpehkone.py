#!/usr/bin/python3

import sys

if len(sys.argv) != 2 or not sys.argv[1]:
	print("usage: " + sys.argv[0] + " <a-zA-Z string>")
	exit(0)
for i in sys.argv[1]:
	if not (i.isalpha() and ord(i) < 128) and i != ' ':
		print("usage: " + sys.argv[0] + " <a-zA-Z string>")
		exit(0)
sys.argv[1] = sys.argv[1].lower()
for i in sys.argv[1]:
	if i == "a":
		print(".-", end =""),
	elif i == "b":
		print("-...", end =""),
	elif i == "c":
		print("-.-.", end =""),
	elif i == "d":
		print("-..", end =""),
	elif i == "e":
		print(".", end =""),
	elif i == "f":
		print("..-.", end =""),
	elif i == "g":
		print("--.", end =""),
	elif i == "h":
		print("....", end =""),
	elif i == "i":
		print("..", end =""),
	elif i == "j":
		print(".---", end =""),
	elif i == "k":
		print("-.-", end =""),
	elif i == "l":
		print(".-..", end =""),
	elif i == "m":
		print("--", end =""),
	elif i == "n":
		print("-.", end =""),
	elif i == "o":
		print("---", end =""),
	elif i == "p":
		print(".--.", end =""),
	elif i == "q":
		print("--.-", end =""),
	elif i == "r":
		print(".-.", end =""),
	elif i == "s":
		print("...", end =""),
	elif i == "t":
		print("-", end =""),
	elif i == "u":
		print("..-", end =""),
	elif i == "v":
		print("...-", end =""),
	elif i == "w":
		print(".--", end =""),
	elif i == "x":
		print("-..-", end =""),
	elif i == "y":
		print("-.--", end =""),
	elif i == "z":
		print("--..", end =""),
	else:
		print(" ", end =""),
print()
