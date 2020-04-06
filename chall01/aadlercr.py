#!/usr/bin/python3

import sys


def printMorse(message):
    morse = [
        '.-',
        '-...',
        '-.-.',
        '-..',
        '.',
        '..-.',
        '--.',
        '....',
        '..',
        '.---',
        '-.-',
        '.-..',
        '--',
        '-.',
        '---',
        '.--.',
        '--.-',
        '.-.',
        '...',
        '-',
        '..-',
        '...-',
        '.--',
        '-..-',
        '-.--',
        '--..'
    ]
    res = ''
    for letter in message:
        if 97 <= ord(letter.lower()) <= 122:
            res = res + morse[ord(letter.lower()) - 97]
        else:
            if ord(letter) == 32:
                res = res + ' '
            else:
                print("usage: ./aadlercr.py <a-zA-Z string>")
                return
    print(res if len(res) else "usage: ./aadlercr.py <a-zA-Z string>")


def main():
    if not len(sys.argv) == 2:
        print("usage: ./aadlercr.py <a-zA-Z string>")
    else:
        printMorse(sys.argv[1])
    return


if __name__ == '__main__':
    main()