#!/usr/bin/env python3

import sys

def usage():
        # there, this better get the right thing...
        sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

def input_test():
        height = len(sys.argv) - 1
        if height > 20:
                usage()
        for arg in sys.argv[1:]:
                # is good length
                if len(arg) != height:
                        usage()
                # is only numeric
                if arg.isnumeric() == False:
                        usage()

def snail_mail():
        shell = []
        # arguments  into arrays
        for string in sys.argv[1:]:
                shell.append(list(string))
        # loop the arrays till we find the end
        while len(shell) > 1:
                # print the top row
                for num in shell[0]:
                        print(num + ", ", end = '')
                shell.pop(0)
                # print the right most column
                width = len(shell[0]) - 1
                for row in shell:
                        print(row[width] + ", ", end = '')
                        row.pop(width)
                # print the bottom row
                width -= 1
                # for even numbered squares, different ending
                if width < 1:
                        break
                height = len(shell) - 1
                while width >= 0:
                        print(shell[height][width] + ", ", end = '')
                        width -= 1
                shell.pop(height)
                # print the left most column
                height -= 1
                while height >= 0:
                        print(shell[height][0] + ", ", end = '')
                        shell[height].pop(0)
                        height -= 1
        # print the last remaining number
        print(shell[0][0])

def main():
        if len(sys.argv) > 1:
                input_test()
                snail_mail()
        else:
                usage()
        

if __name__ == '__main__':
	main()
