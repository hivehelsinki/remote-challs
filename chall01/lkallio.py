#!/usr/bin/python

import sys

output = []
alpha_tree = "/etianmsurwdkgohvfulapjbxcyzq"

def		print_usage():
	print 'usage: ./lkallio.py <a-zA-Z string>'
	exit(0)

# We search the string "alpha_tree" such that every recursive step
# "left" (i is uneven) signifies a dot, whereas a step "right"
# signifies a line. When we hit the character, we either move on to the next 
# character of the converted string or we return 1 and begin appending dots or
# lines every step of the way back from the recursion, creating a reversed string of morse code.
# The source for this idea is this image:
# https://qph.fs.quoracdn.net/main-qimg-fd6688d09555dd7cf9221e7396377c5b

def		search_morse_tree(inp, i, j):
	if (i > 28):
		return (0)
	elif (i and (alpha_tree[i] == inp[j]
	or alpha_tree[i].upper() == inp[j]
	or inp[j] == ' ')):
		if (j < len(inp) - 1):
			if (not search_morse_tree(inp, 0, j + 1)):
				print_usage()
	elif (i and (inp[j] == ' ')):
		if (not search_morse_tree(inp, 0, j + 1)):
				print_usage()
	elif (not search_morse_tree(inp, i * 2 + 1, j)
	and not search_morse_tree(inp, i * 2 + 2, j)):
		return (0)
	if (i and inp[j] != ' '):
		output.append('.' if i % 2 else '-')
	elif (i):
		output.append(' ')
	return (1)

if (len(sys.argv) != 2 or not len(sys.argv[1])
or not search_morse_tree(sys.argv[1], 0, 0)):
	print_usage()

print ''.join(output[::-1])
