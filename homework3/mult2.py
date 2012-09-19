#ECE2524 Homework 3 Problem 2 Laurin Mordhorst

import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description='Multiply numbers')
parser.add_argument('filenames', action='store', type=str, nargs='*')
parser.add_argument('--ignore-blank', action='store_true', dest='blank')
parser.add_argument('--ignore-non-numeric', action='store_true', dest='non_numeric')
arguments = parser.parse_args()
result = 1.0
for line in fileinput.input(arguments.filenames): 
    try:
        number = float(line)
        result *= number
    except ValueError, vE:
        if line == "\n":
            if arguments.blank == False:
                print(result)
                result = 1
        else:
            if arguments.non_numeric == False:
                print >> sys.stderr, vE
                sys.exit(1)
print(result)


