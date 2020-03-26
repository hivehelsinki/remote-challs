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
	print("usage: ./sadawi.py <a-zA-Z string>")
	sys.exit()

if len(sys.argv) != 2:
	error()

result = ""
if not sys.argv[1]:
	error()
for char in sys.argv[1]:
	char = char.upper()
	asciiValue = ord(char)
	if not 65 <= asciiValue <= 90 and char != " ":
		error()
	if char == " ":
		result += " "
	else:
		result += format[asciiValue - 65]
print (result)