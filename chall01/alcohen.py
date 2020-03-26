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
string_alpha_or_spaces = all(x.isalpha() or x.isspace() for x in sys.argv[1])
if (len(sys.argv) != 2 or not string_alpha_or_spaces or not sys.argv[1]):
    print("usage: ./alcohen.py <a-zA-Z string>")
    exit()
codes = c.split()
alph = list(string.ascii_lowercase)
d = dict(zip(alph, codes))


for x in str(sys.argv[1]).lower():
    if (x == " "):
        print(" ", end="")
    else:
        print(d[x], end="")
print()
