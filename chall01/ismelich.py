#!/usr/bin/env python3

import sys

morse_code = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
}
str = sys.argv[1]
for x in str:
    av = ord(x)
    if av < 32 or 32 < av < 65 or 90 < av < 97 or av > 122:
        print('usage: ./ismelich.py <a-zA-Z string>')
        exit(1)

if len(sys.argv) != 2:
    print ('usage: ./ismelich.py <a-zA-Z string>')
    sys.exit(1)

def encryptor(text):
    encrypted_text = ""
    for letters in text:
        if letters != " ":
            encrypted_text = encrypted_text + morse_code.get(letters)
        else:
            encrypted_text += " "
    print(encrypted_text)


text_to_encrypt = " ".join(sys.argv[1:]).upper()
encryptor(text_to_encrypt)