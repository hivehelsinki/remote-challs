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
            exit(1)
    print (ret)

def main():
    if len (sys.argv) == 2:
        tinnitus(sys.argv[1].lower())
    else:
        print ('usage: ./vtran.py <a-zA-Z string>')
        exit(1)
main()