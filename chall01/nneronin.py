#!/usr/bin/env python3
import sys

CHEAT_SHEET = {'a':'.-', 'b':'-...', 
               'c':'-.-.', 'd':'-..',
               'e':'.', 'f':'..-.',
               'g':'--.', 'h':'....', 
               'i':'..', 'j':'.---',
               'k':'-.-', 'l':'.-..',
               'm':'--', 'n':'-.',
               'o':'---', 'p':'.--.',
               'q':'--.-', 'r':'.-.',
               's':'...', 't':'-',
               'u':'..-', 'v':'...-',
               'w':'.--', 'x':'-..-',
               'y':'-.--', 'z':'--..'}

def error_message():
    print ("usage:", sys.argv[0], "<a-zA-Z string>")
    quit()

if len(sys.argv) != 2:
    error_message()
morse = ''
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in sys.argv[1]:
    if alphabet.find(letter.lower()) == -1 and letter != ' ':
        error_message()
    if letter != ' ':
        morse += CHEAT_SHEET[letter.lower()]
    else:
        morse += ' '
if morse == '':
    error_message()
print (morse)
