MORSE_DICTIONARY = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..'}

import sys

message = ''
result = ''

if len(sys.argv) != 2 :
    print('usage: ./xlogin.py <a-zA-Z string>')
    quit()
message = sys.argv[1]
print (message)
for letter in message :
    if (letter >= 'A' and letter <= 'Z') or (letter >= 'a' and letter <= 'z'):
        result += MORSE_DICTIONARY[letter]
    elif letter == ' ' :
        result += ' '
    else :
        print ('usage: ./xlogin.py <a-zA-Z string>')
        quit()
print(result)
