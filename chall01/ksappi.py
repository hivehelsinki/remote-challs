#!/usr/bin/python3
import sys

charset = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
	".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
	"...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

def main():
	output = ""
	if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
		print("usage: ./ksappi.py <a-zA-Z string>")
		return
	for char in sys.argv[1]:
		if char.isalpha():
			output += charset[ord(char.lower()) - ord('a')]
		elif char == " ":
			output += " "
		else:
			print("usage: ./ksappi.py <a-zA-Z string>")
			return
	print(output)

if __name__ == "__main__":
	main()