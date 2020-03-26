# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    asolopov.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asolopov <asolopov@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/26 19:14:47 by asolopov          #+#    #+#              #
#    Updated: 2020/03/26 20:18:52 by asolopov         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse_dict = {
"a": ".-",
"b": "-...",
"c": "-.-.",
"d": "-..",
"e": ".",
"f": "..-.",
"g": "--.",
"h": "....",
"i": "..",
"j": ".---",
"k": "-.-",
"l": ".-..",
"m": "--",
"n": "-.",
"o": "---",
"p": ".--.",
"q": "--.-",
"r": ".-.",
"s": "...",
"t": "-",
"u": "..-",
"v": "...-",
"w": ".--",
"x": "-..-",
"y": "-.--",
"z": "--.."
}

def usage():
	print(f"usage: {sys.argv[0]} <a-zA-Z string>")
	exit()	

def check_chars(word, morse_dict):
	for x in word:
		if x.isalpha() == False:
			if x.isspace() == False:
				usage()
		else:
			if x not in morse_dict:
				usage()

if (len(sys.argv)) != 2:
	usage()
else:
	word = sys.argv[1].lower()
	check_chars(word, morse_dict)
	for x in word:
		if (x.isalpha()):
			print(morse_dict[x], end='')
		elif (x.isspace()):
			print(" ", end='')
		else:
			usage()
print()
			