#!/usr/bin/env python3

from re import split
from sys import argv

crit = float(argv[1])

split_sets = {x:set() for x in range(10)}

for i in range(10):
    with open("%d.train.gini.reformat" % i) as f:
        f.readline()
        for line in f:
            col, split1, split2 = split(r'\s+', line.strip())
            col = int(col)
            split1, split2 = float(split1), float(split2)
            if split1 >= crit or split2 >= crit:
                split_sets[i] |= set([col])
            #else: print("NOPE")

final_set = split_sets[0]

for i in range(1, 5):
    final_set &= split_sets[i]

print("NUMBER OF FEATURES IN ALL SPLITS: %d" % len(final_set))

for col in final_set:
    print(col)
