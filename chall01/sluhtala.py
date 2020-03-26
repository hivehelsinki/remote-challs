import sys

def print_usage():
    print("usage: ./sluhtala.py <a-zA-Z string>")
    exit()

if len(sys.argv) != 2:
    print_usage()
arglen = len(sys.argv[1])
if arglen == 0:
    print_usage()
alphabet = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ '
for i in range(arglen):
    if sys.argv[1][i]  not in alphabet:
        print_usage()
morse = ['.-','-...','-.-.',
'-..','.','..-.','--.','....',
'..','.---','-.-','.-..','--',
'-.','---','.--.','--.-','.-.',
'...','-','..-','...-','.--','-..-',
'-.--','--..']
for i in range(arglen):
    letter = sys.argv[1][i]
    if letter.isupper():
        letter = letter.lower()
    if (sys.argv[1][i] == ' '):
        print(' ', end='')
    else:
        print(morse[ord(letter) - 97], end='')
print('')
