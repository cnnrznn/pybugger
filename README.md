# pybugger
Easily insert debugging print statements into C / C++ codes.

When debugging segmentation faults and other common
C/C++ errors, it is often helpful to insert print
statements into code to quickly determine the point
of failure. This is meant to be a simple tool to
do exactly that. Instead of having to manually insert
print statements, this code will parse the code file
and insert debugging statements at the beginning of
all functions and branching statements. Later, one
can use the unique print statements to pinpoint the line
of failure in the code.
