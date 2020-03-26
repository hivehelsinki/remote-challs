#!/usr/bin/env python3
import sys

alpha = {
        'a' : ".-",
        'b' : "-...",
        'c' : "-.-.",
        'd' : "-..",
        'e' : ".",
        'f' : "..-.",
        'g' : "--.",
        'h' : "....",
        'i' : "..",
        'j' : ".---",
        'k' : "-.-",
        'l' : ".-..",
        'm' : "--",
        'n' : "-.",
        'o' : "---",
        'p' : ".--.",
        'q' : "--.-",
        'r' : ".-.",
        's' : "...",
        't' : "-",
        'u' : "..-",
        'v' : "...-",
        'w' : ".--",
        'x' : "-..-",
        'y' : "-.--",
        'z' : "--..",
        ' ' : " "}
if len(sys.argv) == 2 and len(sys.argv[1]) > 0 and all(i.isalpha() or i.isspace() for i in sys.argv[1]):
    for letter in sys.argv[1]:
        print(alpha[letter.lower()], end = '')
    print('')
else:
    print ("usage:", sys.argv[0], "<a-zA-Z string>")
