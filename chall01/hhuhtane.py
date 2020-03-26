# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hhuhtane.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hhuhtane <hhuhtane@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/26 15:47:35 by hhuhtane          #+#    #+#              #
#    Updated: 2020/03/26 16:51:09 by hhuhtane         ###   ########.fr        #
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

if len(sys.argv) == 2:
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
else:
    print("usage: ./hhuhtane.py <a-zA-Z string>")

