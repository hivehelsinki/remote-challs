#!/usr/bin/env python3

import sys

def intp_to_mos(av):
	for i in range(len(av)):
		if (av[i] == 'A') | (av[i] == 'a'):
			print('.-', end='')
		elif (av[i] == 'B') | (av[i] == 'b'):
			print('-...', end='')
		elif (av[i] == 'C') | (av[i] == 'c'):
			print('-.-.', end='')
		elif (av[i] == 'D') | (av[i] == 'd'):
			print('-..', end='')
		elif (av[i] == 'E') | (av[i] == 'e'):
			print('.', end='')
		elif (av[i] == 'F') | (av[i] == 'f'):
			print('..-.', end='')
		elif (av[i] == 'G') | (av[i] == 'g'):
			print('--.', end='')
		elif (av[i] == 'H') | (av[i] == 'h'):
			print('....', end='')
		elif (av[i] == 'I') | (av[i] == 'i'):
			print('..', end='')
		elif (av[i] == 'J') | (av[i] == 'j'):
			print('.---', end='')
		elif (av[i] == 'K') | (av[i] == 'k'):
			print('-.-', end='')
		elif (av[i] == 'L') | (av[i] == 'l'):
			print('.-..', end='')
		elif (av[i] == 'M') | (av[i] == 'm'):
			print('--', end='')
		elif (av[i] == 'N') | (av[i] == 'n'):
			print('-.', end='')
		elif (av[i] == 'O') | (av[i] == 'o'):
			print('---', end='')
		elif (av[i] == 'P') | (av[i] == 'p'):
			print('.--.', end='')
		elif (av[i] == 'Q') | (av[i] == 'q'):
			print('--.-', end='')
		elif (av[i] == 'R') | (av[i] == 'r'):
			print('.-.', end='')
		elif (av[i] == 'S') | (av[i] == 's'):
			print('...', end='')
		elif (av[i] == 'T') | (av[i] == 't'):
			print('-', end='')
		elif (av[i] == 'U') | (av[i] == 'u'):
			print('..-', end='')
		elif (av[i] == 'V') | (av[i] == 'v'):
			print('...-', end='')
		elif (av[i] == 'W') | (av[i] == 'w'):
			print('.--', end='')
		elif (av[i] == 'X') | (av[i] == 'x'):
			print('-..-', end='')
		elif (av[i] == 'Y') | (av[i] == 'y'):
			print('-.--', end='')
		elif (av[i] == 'Z') | (av[i] == 'z'):
			print('--..', end='')
		elif av[i] == ' ':
		 	print(av[i], end='')
	print('')
		
av = sys.argv[1:]
if len(av) == 1:
	if len(av[0]) == 0:
		print('usage: ', sys.argv[0], '<a-zA-Z string>')
		exit()
	for i in range(len(av[0])):
		if not(('A' <= av[0][i] <= 'Z') | ('a' <= av[0][i] <= 'z')  \
				| (av[0][i] == ' ')):
			print('usage: ', sys.argv[0], '<a-zA-Z string>')
			exit()
	else:
		intp_to_mos(av[0])
else:
	print('usage: ', sys.argv[0], '<a-zA-Z string>')
