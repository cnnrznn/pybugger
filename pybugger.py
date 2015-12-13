#!/usr/bin/python

# Author: Connor Zanin
# Description:
#   When debugging segmentation faults and other common
#   C/C++ errors, it is often helpful to insert print
#   statements into code to quickly determine the point
#   of failure. This is meant to be a simple tool to
#   do exactly that. Instead of having to manually insert
#   print statements, this code will parse the code file
#   and insert debugging statements at the beginning of
#   all functions and branching statements. Later, one
#   can use the unique print statements to pinpoint the line
#   of failure in the code.
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
    lines[i] = lines[i].strip('\n').split('{')

# generate identifiers
alphabet = string.ascii_lowercase

# insert printf statements after '{'
for i in xrange(len(lines)):
    if len(lines[i]) > 2:
        # TODO insert printf
        pass
