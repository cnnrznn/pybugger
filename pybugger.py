#!/usr/bin/python

# Author: Connor Zanin
# Input: name of C/C++ code file
# Output: C/C++ code file with debugging printf statements

import sys
import string

#################
### FUNCTIONS ###
#################

def create_print(string, num):
    return "printf(\"" + sys.argv[1] + "_" + \
            string + str(num) + "\\n\");"

def mode_main(lines, i):
    global debug_string
    global debug_alph
    global debug_num
    global mode
    if lines[i].find('{') > -1:
        if "switch" in lines[i]:
            mode = _switch
            return
        index = lines[i].find('{') + 1
        debug_string += alphabet[debug_alph[debug_string]]
        debug_alph[debug_string] = 0
        debug_num[debug_string] = 0
        print lines[i][:index] + \
                create_print(debug_string, debug_num[debug_string]) + \
                lines[i][index:]
    elif lines[i].find('}') > -1:
        index = lines[i].find('}') + 1
        debug_string = debug_string[:-1]
        if debug_string != "":
            debug_alph[debug_string] += 1
            debug_num[debug_string] += 1
            print lines[i][:index] + \
                    create_print(debug_string, debug_num[debug_string]) + \
                    lines[i][index:]
        else:
            print lines[i]
    else:
        print lines[i]

##############
### SCRIPT ###
##############

# miscellaneous variables
_main = 0
_switch = 1
mode = _main

# open and read lines of code file
inf = open(sys.argv[1])
lines = inf.readlines()
inf.close()

# pre-process file
for i in xrange(len(lines)):
    lines[i] = lines[i].strip('\n')

# generate identifiers
alphabet = string.ascii_lowercase

# initialize stack
debug_string = ""       # current location in stack
debug_alph = dict()     # index of next char to use
debug_num = dict()      # number associated with each location in stack
debug_alph[""] = 0

# insert printf statements
for i in xrange(len(lines)):
    if mode == _main:
        mode_main(lines, i)
