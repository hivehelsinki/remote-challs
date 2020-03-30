#!/usr/bin/env python3
import string
import sys

def error():
    print("usage: ./alcohen.py <a-zA-Z string>")
    exit()

# Morse codes in order from A to Z
morse_codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

if (len(sys.argv) != 2): # Only accept one argument
    error()

# alphabet contains letters [a-z] and a space
alphabet = list(string.ascii_lowercase + ' ')
string_to_convert = sys.argv[1].lower()

# Check that string to convert isn't empty and only contains characters that are in alphabet.
string_is_a_to_z_or_spaces = all(letter in alphabet for letter in string_to_convert) 
if (not string_is_a_to_z_or_spaces or not string_to_convert):
    error()

# Combine letters and morse codes to a dictionary. A letter can be looked up to receive the corresponding morse code.
alphabet_morse_dict = dict(zip(alphabet, morse_codes))
alphabet_morse_dict[' '] = ' '

for letter in string_to_convert:
        print(alphabet_morse_dict[letter], end='')
print()