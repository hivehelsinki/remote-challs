#! /usr/bin/python3

import sys

format = """.-
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
--..""".split()

def error():
	print("usage: ./xlogin.py <a-zA-Z string>")
	sys.exit()

if len(sys.argv) != 2:
	error()

result = ""
input = sys.argv[1]
if not input:
	error()
for c in input:
	c = c.upper()
	if not 65 <= ord(c) <= 90 and c != " ":
		error()
	if c == " ":
		result += " "
	else:
		result += format[ord(c) - 65]
print (result)