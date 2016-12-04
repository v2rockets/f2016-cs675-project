#!/usr/bin/env python3

### kathryn gorski
### cs675 machine learning
### assignment 5: CART

from sys import argv
from re import split


### functions for handling raw data

def standardize_data(d_f):
    """Change raw data file into a nested array."""
    with open(d_f) as f: 
        return [[float(datum) for datum in split(r'\s+', line.strip())]
                for line in f]

def standardize_labels(l_f):
    """Change label file into a nested array."""
    with open(l_f) as f:
        return [[int(datum) for datum in split(r'\s+', line.strip())]
                for line in f]

if len(argv) != 3:
    print("""Please run in the format
    script data training_labels""")
    quit()
script, data_f, labels_f = argv

data = standardize_data(data_f)
labels = standardize_labels(labels_f)

ncol = len(data[0])
nrow = len(labels)
nc1 = len([0 for n in range(nrow) if labels[n][0] == 0])
nc2 = len([0 for n in range(nrow) if labels[n][0] == 1])

best_splits = [0] * ncol
best_gini = [0] * ncol

for j in range(ncol):
    col_vect = list(zip(*data))[j]
    n_split = 20
    col_range = abs(max(col_vect) - min(col_vect))
    potential_splits = [min(col_vect) + col_range/n_split]
    for i in range(1,20):
        potential_splits.append(potential_splits[i-1] + col_range / n_split)
    split_hash = dict()
    for split in potential_splits:
        c1_corr = 0
        c1_incorr = 0
        c2_corr = 0
        c2_incorr = 0
        for i in range(nrow):
            if data[i][j] < split and labels[i][0] == 0:
                c1_corr += 1
            elif data[i][j] >= split and labels[i][0] == 1:
                c2_corr += 1
        c1_incorr = nc1 - c1_corr
        c2_incorr = nc2 - c2_corr
        c1predict_size = c1_corr + c2_incorr
        c2predict_size = nrow - c1predict_size
        if c1predict_size == 0: gini1 = 0
        else: gini1 = c1predict_size / nrow * (c1_corr / c1predict_size) * \
                (1 - (c1_corr / c1predict_size))
        if c2predict_size == 0: gini2 = 0
        else: gini2 = c2predict_size / nrow * (c1_incorr / c2predict_size) * \
                (1 - (c1_incorr / c2predict_size))
        gini = gini1 + gini2
        split_hash[split] = gini
    #print(potential_splits)
    #print("CURRENT COLUMN:", j)
    gini_hash = dict()
    for key in potential_splits:
        #print(key, split_hash[key])
        new_key = split_hash[key]
        if new_key in gini_hash: next
        else: gini_hash[new_key] = key
    best_gini_t = min(list(gini_hash.keys()))
    best_split_t = gini_hash[best_gini_t]
    best_gini[j] = best_gini_t
    best_splits[j] = best_split_t

#print(best_gini)
#print(min(best_gini))
#print(best_splits)

best_col = best_gini.index(min(best_gini))
best_split = best_splits[best_col]

print("best column: %d, best split: %0.8f, best gini: %0.6f" % 
        (best_col, best_split, min(best_gini)))
