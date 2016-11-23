#!/usr/bin/env python3

from sys import argv
from re import split
from math import sqrt

script, d_f = argv

with open(d_f) as f:
    data = [[float(datum) for datum in split(r'\s+', line.strip())] for line in f]
counter = 0

for col in zip(*data):
    avg = sum(col) / len(col)
    variance = (sum([(col[i] - avg) ** 2 for i in range(len(col))])) / len(col)
    std_dev = sqrt(variance)
    print("%d var %f std_dev %f" % (counter, variance, std_dev))
    counter += 1
