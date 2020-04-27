import sys

def error_msg():
	print("usage: ./tmaarela.py <1-9 squared_rows...>")
	quit()

def error_check(args):
	if (len(args) <= 0):
		error_msg()
	for x in range(len(args)):
		if len(args[x]) != len(args):
			error_msg()
		if not args[x].isnumeric():
			error_msg()

def make_final_print(args, startpos):
	fstring = ""
	if int(len(args) / 2) - startpos <= 0 and len(args) % 2 != 0:
		fstring = args[int((len(args)) / 2)][int((len(args)) / 2)]
		return fstring
	l = len(args) - startpos
	for hor in range(startpos, l):
		fstring += args[startpos][hor] + ", "
	for ver in range(startpos + 1, l):
		fstring += args[ver][l - 1] + ", "
	for hor_bot in range(l - 1, startpos, -1):
		fstring += args[l - 1][hor_bot - 1] + ", "
	for ver_first in range(l - 1, startpos + 1, -1):
		fstring += args[ver_first - 1][startpos] + ", "
	return fstring

args = sys.argv[1:]
fstring = ""
error_check(args)
for loop in range(int(len(args)/2 + 1)):
	fstring += make_final_print(args, loop)
if len(args) % 2 == 0:
	fstring = fstring[0:-2]
print(fstring + "\n")
