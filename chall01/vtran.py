#!/usr/bin/python3
import sys

tittut = {
    'a': ".-",
    'b': "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': ".---",
    'k': "-.-",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    's': "...",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    'x': "-..-",
    'y': "-.--",
    'z': "--..",
    ' ': " "
}

def tinnitus(str):
    ret = ""
    for i in str:
        try:
            ret += tittut[i]
        except KeyError:
            print ('usage: ./vtran.py <a-zA-Z string>')
            sys.exit(1)
    if len(str) > 0:
        print (ret)

def usage():
    print ('usage: ./vtran.py <a-zA-Z string>')
    sys.exit(1)

def main():
    if len (sys.argv) == 2:
        tinnitus(sys.argv[1].lower())
    else:
        usage()
main()