#ECE2524 Homework 3 Problem 2 Laurin Mordhorst

import argparse
import sys

parser = argparse.ArgumentParser(description='Multiply numbers')
parser.parse_args()

result = 1.0
try:
    input = raw_input()
except EOFError:
    sys.exit(1)
while(input != "^D"):
    try:
        number = float(input)
        result *= number
    except ValueError, vE:
        if input == "":
            print(result)
            result = 1
        else:
            print >> sys.stderr, vE
            sys.exit(2)
    try:
        input = raw_input()
    except EOFError:
        break
print(result)
