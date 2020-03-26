#!/usr/bin/python3
import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

if len(sys.argv) < 2:
	quit()
for arg_ch in sys.argv[1]:
	aplha_i = alphabet.find(arg_ch.lower())
	if aplha_i == 0:
		print (".-", end = "")
	if aplha_i == 1:
		print ("-...", end = "")
	if aplha_i == 2:
		print ("-.-.", end = "")
	if aplha_i == 3:
		print ("-..", end = "")
	if aplha_i == 4:
		print (".", end = "")
	if aplha_i == 5:
		print ("..-.", end = "")
	if aplha_i == 6:
		print ("--.", end = "")
	if aplha_i == 7:
		print ("....", end = "")
	if aplha_i == 8:
		print ("..", end = "")
	if aplha_i == 9:
		print (".---", end = "")
	if aplha_i == 10:
		print ("-.-", end = "")
	if aplha_i == 11:
		print (".-..", end = "")
	if aplha_i == 12:
		print ("-- ", end = "")
	if aplha_i == 13:
		print ("-.", end = "")
	if aplha_i == 14:
		print ("---", end = "")
	if aplha_i == 15:
		print (".--.", end = "")
	if aplha_i == 16:
		print ("--.-", end = "")
	if aplha_i == 17:
		print (".-.", end = "")
	if aplha_i == 18:
		print ("...", end = "")
	if aplha_i == 19:
		print ("-", end = "")
	if aplha_i == 20:
		print ("..-", end = "")
	if aplha_i == 21:
		print ("...-", end = "")
	if aplha_i == 22:
		print (".--", end = "")
	if aplha_i == 23:
		print ("-..-", end = "")
	if aplha_i == 24:
		print ("-.--", end = "")
	if aplha_i == 25:
		print ("--..", end = "")
print ("")