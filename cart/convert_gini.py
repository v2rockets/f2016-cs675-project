#!/usr/bin/env python3

from sys import argv
from re import split

script, gini_in, gini_out = argv

f_out = open(gini_out, "w")
f_out.write("COL\tFIRST_SPLIT\tSECOND_SPLIT\n")

with open(gini_in) as f_in:
    for line in f_in:
        info = split(r'\s+', line.strip())
        f_out.write("%s\t%s\t%s\n" % (info[0], info[2], info[4]))

f_out.close()
