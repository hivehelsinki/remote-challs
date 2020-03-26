#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hhuhtane.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hhuhtane <hhuhtane@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/26 15:47:35 by hhuhtane          #+#    #+#              #
#    Updated: 2020/03/26 19:31:19 by hhuhtane         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arg_i = 0
i = 0
morse = ""
codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
         '..-', '...-', '.--', '-..-', '-.--', '--..']

if ( (len(sys.argv) != 2) or ( sys.argv[1].isalpha() == False)):
        print("usage: ./hhuhtane.py <a-zA-Z string>")
else:
    while arg_i < len(sys.argv[1]):
        i = 0
        while i < 26:
            if alphabet[i] == sys.argv[1][arg_i]:
                morse += codes[i]
            if capital[i] == sys.argv[1][arg_i]:
                morse += codes[i]
            i += 1
        arg_i += 1
    print(f"{morse}")

