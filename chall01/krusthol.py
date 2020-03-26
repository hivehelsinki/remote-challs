#!/usr/bin/python3
import sys
import string

def bad_character(str):
    good = set(string.ascii_lowercase + ' ')
    for c in str:
        if c not in good:
            return True
    return False

if len(sys.argv) != 2:
    sys.exit("usage: ./krusthol.py <a-zA-Z string>")
arg = sys.argv[1].lower()
if len(arg) == 0 or bad_character(arg):
    sys.exit("usage: ./krusthol.py <a-zA-Z string>")
for c in arg:
    if c == 'a':
        sys.stdout.write('.-')
    elif c == 'b':
        sys.stdout.write('-...')
    elif c == 'c':
        sys.stdout.write('-.-.')
    elif c == 'd':
        sys.stdout.write('-..')
    elif c == 'e':
        sys.stdout.write('.')
    elif c == 'f':
        sys.stdout.write('..-.')
    elif c == 'g':
        sys.stdout.write('--.')
    elif c == 'h':
        sys.stdout.write('....')
    elif c == 'i':
        sys.stdout.write('..')
    elif c == 'j':
        sys.stdout.write('.---')
    elif c == 'k':
        sys.stdout.write('-.-')
    elif c == 'l':
        sys.stdout.write('.-..')
    elif c == 'm':
        sys.stdout.write('--')
    elif c == 'n':
        sys.stdout.write('-.')
    elif c == 'o':
        sys.stdout.write('---')
    elif c == 'p':
        sys.stdout.write('.--.')
    elif c == 'q':
        sys.stdout.write('--.-')
    elif c == 'r':
        sys.stdout.write('.-.')
    elif c == 's':
        sys.stdout.write('...')
    elif c == 't':
        sys.stdout.write('-')
    elif c == 'u':
        sys.stdout.write('..-')
    elif c == 'v':
        sys.stdout.write('...-')
    elif c == 'w':
        sys.stdout.write('.--')
    elif c == 'x':
        sys.stdout.write('-..-')
    elif c == 'y':
        sys.stdout.write('-.--')
    elif c == 'z':
        sys.stdout.write('--..')
    elif c == ' ':
        sys.stdout.write(' ')
print("")
sys.exit(0)