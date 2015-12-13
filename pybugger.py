#!/usr/bin/python

# Author: Connor Zanin
# Input: name of C/C++ code file
# Output: C/C++ code file with debugging printf statements

import sys
import string

# open and read lines of code file
inf = open(sys.argv[1])
lines = inf.readlines()
inf.close()

# pre-process file
for i in xrange(len(lines)):
    lines[i] = lines[i].strip('\n')

# generate identifiers
alphabet = string.ascii_lowercase
debug_string = ""       # current location in stack
debug_num = dict()      # number associated with each location in stack
debug_alph = dict()     # index of next char to use
debug_alph[""] = 0

# insert printf statements after '{'
for i in xrange(len(lines)):
    if lines[i].find('{') > -1:
        pass
    elif lines[i].find('}') > -1:
        pass
