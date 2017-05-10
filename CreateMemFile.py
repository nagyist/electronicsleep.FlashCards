#!/usr/bin/python

# Author: Chris Robertson https://github.com/electronicsleep
# Date: 06/17/2015
# Purpose: Generate a memorize.txt file for FlashCards.py
# Released under the BSD license

# Running:
# python CreateMemFile.py

# IMPORT STANDARD FUNCTIONS

import sys

# APPEND TO MEMORIZE FILE

f = open('memorize.txt', 'a')
f.write("\n")
f.write("#MATH QUESTIONS FOR MEMORIZING")
f.write("\n")
f.write("\n")

# FOR SIMPLE TIMES TABLES

for x in range(2, 10):
    for y in range(2, 10):
        times = x * y
        xx = str(x)
        yy = str(y)
        times2 = str(times)
        f.write("Q. " + xx + " * " + yy + "\n")
        f.write("A. " + times2 + "\n")
        f.write("\n")

# FOR DIFFICULT TIMES TABLES

for x in range(11, 20):
    for y in range(1, 25):
        times = x * y
        xx = str(x)
        yy = str(y)
        times2 = str(times)
        f.write("Q. " + xx + " * " + yy + "\n")
        f.write("A. " + times2 + "\n")
        f.write("\n")
 
# END OF SCRIPT
sys.exit(0)
