#!/usr/local/bin/python3

# import sys for reading program arguments and regular expressions for filtering away non-ascii
import sys, re

def encoder(encodable):
    # morse letters in order from a to z, \n as the separator
    rawMorse = """.-
                -... 
                -.-. 
                -.. 
                . 
                ..-. 
                --. 
                .... 
                .. 
                .--- 
                -.- 
                .-.. 
                -- 
                -. 
                --- 
                .--. 
                --.- 
                .-. 
                ... 
                - 
                ..- 
                ...- 
                .-- 
                -..- 
                -.-- 
                --.."""

    rawAlphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabet = rawAlphabet.split()
    morse = rawMorse.replace(" ", "").split("\n")

    # merge alphabet and morse lists into a dictionary
    codeBook = dict(zip(alphabet, morse))

    output = ""
    for letter in encodable:
        if letter == " ":
            output += " "
        else:
            output += codeBook[letter]
    return output



"""
Check that 
- there's only one argument,
- argument contains only a to z (no ä, ö, å, etc.) and spaces.
If valid, convert input to lowercase.
"""
if len(sys.argv) == 2 and sys.argv[1].replace(" ", "").isalpha():
    if not re.match(r"^[a-z A-Z]+$", sys.argv[1]):
        print("usage: ./rkyttala.py <a-zA-Z string>")
        quit()
    else:
        progInput = sys.argv[1].lower()
else:
    print("usage: ./rkyttala.py <a-zA-Z string>")
    quit()

encodedMessage = encoder(progInput)
print(encodedMessage)
