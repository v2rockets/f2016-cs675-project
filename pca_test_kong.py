#!/usr/bin/env python2

from __future__ import print_function
from sklearn.decomposition import PCA
import numpy as np
import funct
from sys import argv

script, d_f, l_f, filename = argv

data = funct.Data(d_f, l_f, w0 = False)
labels = data.test_labels
training_data = data.training_rows

training_data = [data.data[i] for i in training_data]
training_labels = [data.labels[i] for i in data.training_rows]

test_data = [data.data[i] for i in labels]

data = np.asarray(training_data)

pca = PCA(n_components = 2)
pca.fit(data)
data_applied = pca.transform(data)

test_data_applied = pca.transform(np.asarray(test_data))

with open(filename + ".results", "w") as f:
    for i in range(len(training_data)):
        f.write("%d %f %f\n" % (training_labels[i], data_applied[i][0], data_applied[i][1]))
