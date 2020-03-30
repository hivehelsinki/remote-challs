#!/usr/bin/python3
import sys

def my_errorMessage():
	print ("usage:", sys.argv[0], "<a-zA-Z string>")
	quit()

alphabet = "abcdefghijklmnopqrstuvwxyz "
morse = ""

if len(sys.argv) != 2:
	my_errorMessage()
for arg_ch in sys.argv[1]:
	alpha_i = alphabet.find(arg_ch.lower())
	if alpha_i == 0:
		morse += ".-"
	elif alpha_i == 1:
		morse += "-..."
	elif alpha_i == 2:
		morse += "-.-."
	elif alpha_i == 3:
		morse += "-.."
	elif alpha_i == 4:
		morse += "."
	elif alpha_i == 5:
		morse += "..-."
	elif alpha_i == 6:
		morse += "--."
	elif alpha_i == 7:
		morse += "...."
	elif alpha_i == 8:
		morse += ".."
	elif alpha_i == 9:
		morse += ".---"
	elif alpha_i == 10:
		morse += "-.-"
	elif alpha_i == 11:
		morse += ".-.."
	elif alpha_i == 12:
		motse += "--"
	elif alpha_i == 13:
		morse += "-."
	elif alpha_i == 14:
		morse += "---"
	elif alpha_i == 15:
		morse += ".--."
	elif alpha_i == 16:
		morse += "--.-"
	elif alpha_i == 17:
		morse += ".-."
	elif alpha_i == 18:
		morse += "..."
	elif alpha_i == 19:
		morse += "-"
	elif alpha_i == 20:
		morse += "..-"
	elif alpha_i == 21:
		morse += "...-"
	elif alpha_i == 22:
		morse += ".--"
	elif alpha_i == 23:
		morse += "-..-"
	elif alpha_i == 24:
		morse += "-.--"
	elif alpha_i == 25:
		morse += "--.."
	elif alpha_i == 26:
		morse += " "
	else:
		my_errorMessage()
print (morse)
