#!/usr/bin/python
import sys

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': ' ',
        }

def main():
    nb = len(sys.argv)

    if nb == 2:
        msg = sys.argv[1]
        if msg == "":
            print "usage: ./gmolin.py <a-zA-Z string>"
            sys.exit()
        for char in msg:
            if char.upper() in CODE:
                continue
            else:
                print "usage: ./gmolin.py <a-zA-Z string>"
                sys.exit()
        for char in msg:
            print CODE[char.upper()],
    else:
        print "usage: ./gmolin.py <a-zA-Z string>"

if __name__ == "__main__":
	main()