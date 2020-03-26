#!/usr/bin/env python3

# Map a char to Morse Code
def encodeToMorse(x): 	
	if x is 'a': 
		return ".-"
	elif x is 'b': 
		return "-..."
	elif x is 'c': 
		return "-.-."
	elif x is 'd': 
		return "-.."
	elif x is 'e': 
		return "."
	elif x is 'f': 
		return "..-."
	elif x is 'g': 
		return "--."
	elif x is 'h': 
		return "...."
	elif x is 'i': 
		return ".."
	elif x is 'j': 
		return ".---"
	elif x is 'k': 
		return "-.-"
	elif x is 'l': 
		return ".-.."
	elif x is 'm': 
		return "--"
	elif x is 'n': 
		return "-."
	elif x is 'o': 
		return "---"
	elif x is 'p': 
		return ".--."
	elif x is 'q': 
		return "--.-"
	elif x is 'r': 
		return ".-."
	elif x is 's': 
		return "..."
	elif x is 't': 
		return "-"
	elif x is 'u': 
		return "..-"
	elif x is 'v': 
		return "...-"
	elif x is 'w': 
		return ".--"
	elif x is 'x': 
		return "-..-"
	elif x is 'y': 
		return "-.--"
	elif x is 'z': 
		return "--.."

# Encode one Char at a time
# concatnate to a string 
# Return encoded string
def morseEncode(string): 
    encodedString = ""
    string = string.lower()
    for char in string:
        if char == " ":
            encodedString += " "
        else:
            encodedString += encodeToMorse(char)
    return encodedString

# Prints Usage 
def printUsage():
    print("usage: ./xlogin.py <a-zA-Z string>")

# Is Alpha or Space and Not other accented letter
# Combining isalpha() and isspace() 'not in' operator
def isAlphaOrSpace(string):
    for char in string:
        if char.isalpha() or char.isspace():
            if char.lower() not in "abcdefghijklmnopqrstuvwxyz ":
                valid = False
                return valid
            else:
                valid = True
        else:
            valid = False
            return valid
    return valid

# Program Starts Here
# Using sys to get access to the argument
# Start Encoding if
# -> ONLY one argument passed
# -> AND it is NOT empty
# -> AND does NOT contain accented characters
# -> Print the returned encoded string
# Otherwise print USAGE
import sys
if len(sys.argv) == 2:
    argument = sys.argv[1]
    if len(argument) != 0 and isAlphaOrSpace(argument):
        print(morseEncode(sys.argv[1]))
    else:
        printUsage()
else:
    printUsage()

