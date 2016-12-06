#!/usr/bin/env python3

from sys import argv

cols = []

with open(argv[1]) as f:
    f.readline()
    for line in f:
        cols += [int(line.strip())]
cols.sort()
for item in cols:
    print(item)
