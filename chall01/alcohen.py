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

def error():
    print("usage: ./alcohen.py <a-zA-Z string>")
    exit()

if (len(sys.argv) != 2):
    error()

alphabet = string.ascii_lowercase
string_a_to_z_or_spaces = all(x.lower() in alphabet or x.isspace() for x in sys.argv[1])
if (not string_a_to_z_or_spaces or not sys.argv[1]):
    error()

codes = c.split()
alph = list(alphabet)
d = dict(zip(alph, codes))

for x in str(sys.argv[1]).lower():
    if (x == " "):
        print(" ", end="")
    else:
        print(d[x], end="")
print()