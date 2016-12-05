#!/usr/bin/env python3

### kathryn gorski
### cs675 machine learning
### assignment 5: CART

from sys import argv
from re import split
import funct


### functions for handling raw data

if len(argv) != 4:
    print("""Please run in the format
    script data training_labels out""")
    quit()
script, data_f, labels_f, out_f = argv

data = funct.Data(data_f, labels_f, w0 = False)

ncol = data.cols
nc1 = data.n_case
nc2 = data.n_control
train_size = nc1 + nc2

best_splits = [0] * ncol
best_gini = [0] * ncol

out = open(out_f, "w")

for j in range(ncol):
    col_vect = data.get_col(j)
    split_hash = dict()
    for split in [0.5, 1.5]:
        c1_corr = 0
        c1_incorr = 0
        c2_corr = 0
        c2_incorr = 0
        for i in data.training_rows:
            if data.data[i][j] < split and data.get_label(i) == 0:
                c1_corr += 1
            elif data.data[i][j] >= split and data.get_label(i) == 1:
                c2_corr += 1
        c1_incorr = nc1 - c1_corr
        c2_incorr = nc2 - c2_corr
        c1predict_size = c1_corr + c2_incorr
        c2predict_size = train_size - c1predict_size
        if c1predict_size == 0: gini1 = 0
        else: gini1 = c1predict_size / train_size * (c1_corr / c1predict_size) * \
                (1 - (c1_corr / c1predict_size))
        if c2predict_size == 0: gini2 = 0
        else: gini2 = c2predict_size / train_size * (c1_incorr / c2predict_size) * \
                (1 - (c1_incorr / c2predict_size))
        gini = gini1 + gini2
        split_hash[split] = gini
    #print(potential_splits)
    #print(j, end = "\t")
    out.write("%d\t" % j)
    gini_hash = dict()
    for key in [0.5, 1.5]:
        out.write("%0.1f %0.9f\t" % (key, split_hash[key]))
        new_key = split_hash[key]
        if new_key in gini_hash: next
        else: gini_hash[new_key] = key
    out.write("\n")
    #best_gini_t = min(list(gini_hash.keys()))
    #best_split_t = gini_hash[best_gini_t]
    #best_gini[j] = best_gini_t
    #best_splits[j] = best_split_t

out.close()

#best_col = best_gini.index(min(best_gini))
#best_split = best_splits[best_col]

#print("best column: %d, best split: %0.8f, best gini: %0.6f" % 
#        (best_col, best_split, min(best_gini)))
