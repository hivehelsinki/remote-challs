import sys
import string


def morse_letter(num):
	num+=1
	code={
	1: ".-",
	2: "-...",
	3: "-.-.",
	4: "-..",
	5: ".",
	6 :"..-.",
	7: "--.",
	8: "....", 
	9: "..", 
	10: ".---", 
	11: "-.-", 
	12: ".-..", 
	13: "--",
	14: "-.", 
	15: "---", 
	16: ".--.", 
	17: "--.-", 
	18: ".-.", 
	19: "...", 
	20: "-", 
	21: "..-", 
	22: "...-", 
	23: ".--", 
	24: "-..-", 
	25: "-.--",
	26: "--..",
	}
	return code.get(num, "invalid")

def morse_word(word):
        morseWord =""
        for c in word:
                if (c.isalpha()) == True:
                        morseWord+=morse_letter(string.ascii_lowercase.index(c.lower()))
                elif (c == ' '):
                        morseWord+=' '
                else:
                        print("usage: ./phakakos.py <a-zA-Z string>")
                        return
        print(morseWord)

if len(sys.argv) == 2:
	morse_word(sys.argv[1])
else:
	print("usage: ./phakakos.py <a-zA-Z string>")