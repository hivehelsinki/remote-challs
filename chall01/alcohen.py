#!/usr/bin/env python3
import string
import sys

c = """.-
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

print(sys.argv[1])
def error():
    print("usage: ./alcohen.py <a-zA-Z string>")
    exit()

if (len(sys.argv) != 2):
    error()

string_alpha_or_spaces = all(x.isalpha() or x.isspace() for x in sys.argv[1])
if (not string_alpha_or_spaces or not sys.argv[1]):
    error()

codes = c.split()
alph = list(string.ascii_lowercase)
d = dict(zip(alph, codes))

for x in str(sys.argv[1]).lower():
    if (x == " "):
        print(" ", end="")
    else:
        print(d[x], end="")
print()