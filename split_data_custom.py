#!/usr/bin/env python3

from sys import argv
from random import sample
from math import floor

l_f = argv[1]
splits = int(argv[2])
out_prefix = argv[3]
num_samples = int(argv[4]) # this is the number to draw from control & positive each, ie 200 = 200 control + 200 positive

with open(l_f) as f:
    data = [line for line in f]

rows = len(data)
test_rows = num_samples

for i in range(splits):
    test_sample = sample(range(rows/2), test_rows) # first half
    test_sample += sample(range(rows/2, rows), test_rows)
    test_sample.sort()
    with open("%s.training.%d" % (out_prefix, i), "w") as f:
        for index in test_sample:
            f.write(data[index])
