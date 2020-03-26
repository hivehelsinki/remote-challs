MORSE = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
        'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
        'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
        'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
        'Z':'--..', 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
        'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..',
        'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',
        'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...',
        't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
        'y':'-.--', 'z':'--..'}

def tomorse(message): 
    output = "" 
    for letter in message: 
        if letter == ' ':
            output += " "
        elif letter >= 'a' and letter <= 'z':
            output += MORSE[letter]
        elif letter >= 'A' and letter <= 'Z':
            output += MORSE[letter]
        else:
            print("usage: ./jhakala.py <a-zA-Z string>")
            return
    print(output)
    return

def main():
    if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
        print("usage: ./jhakala.py <a-zA-Z string>")
        return
    tomorse(argv[1])

if __name__ == '__main__': 
    main() 
