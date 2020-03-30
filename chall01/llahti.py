#!/usr/bin/env python3
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

if len(sys.argv) != 2 or sys.argv[1] == "":
    print("usage: ./xlogin.py <a-zA-Z string>")
    exit()

string = ""

for c in sys.argv[1]:
    if c.isalpha() == False and c != ' ':
        print("usage: ./xlogin.py <a-zA-Z string>")
        exit()
    if c == ' ':
        string += ' '
    elif c.islower():
        string += morse[ord(c) - ord('a')]
    else:
        string += morse[ord(c) - ord('A')]

print(string)