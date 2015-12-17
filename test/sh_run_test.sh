#!/bin/bash

source_file=test.c
debug_file=test_debug.c
debug_bin=test_bin

# create debug file
../pybugger.py $source_file >$debug_file

# compile debug file
gcc -Wall $debug_file -o $debug_bin

# run binary
./$debug_bin
