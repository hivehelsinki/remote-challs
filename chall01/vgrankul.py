#!/usr/bin/env python3
import sys

sos = [
".-",
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

i = 0
letter = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Bletter = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sos_string = ""

if len(sys.argv) != 2:
    print("usage: ./vgrankul.py <a-zA-Z string>")
else:
    string = sys.argv[1]
    if string.replace(' ', '').isalpha() == False:
        print("usage: ./vgrankul.py <a-zA-Z string>")
        exit()
    for let in string:
            i = 0
            while i < 26 and i < 26:
                if letter[i] == let or Bletter[i] == let:
                    sos_string += sos[i]
                i += 1
    print(sos_string)
