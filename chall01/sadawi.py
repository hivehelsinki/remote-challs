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
for char in input:
	char = char.upper()
	asciiValue = ord(char)
	if not 65 <= asciiValue <= 90 and char != " ":
		error()
	if char == " ":
		result += " "
	else:
		result += format[asciiValue - 65]
print (result)