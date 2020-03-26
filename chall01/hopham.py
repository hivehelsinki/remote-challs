#!/usr/bin/python

import sys
import string

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
        ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
        "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

if (len(sys.argv) != 2 or len(sys.argv[1]) == 0):
    print("usage: ./hopham.py <a-zA-Z string>")
    exit()
argument = sys.argv[1]
argument_lowcase = argument.lower()
for character in argument_lowcase:
    if (character not in string.ascii_lowercase and character != " "):
        print("usage: ./hopham.py <a-zA-Z string>")
        exit()

morse_string = dict()
i = 0
for key in string.ascii_lowercase:
    morse_string[key] = morse[i]
    i += 1

for i in argument_lowcase:
    if (i in morse_string):
        sys.stdout.write(morse_string[i])
    else:
        sys.stdout.write(i)
sys.stdout.write("\n")