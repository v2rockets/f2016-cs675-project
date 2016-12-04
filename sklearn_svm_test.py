#!/usr/bin/env python2
##!/usr/bin/env python3

from __future__ import print_function
from sklearn.decomposition import PCA
from sklearn import svm
import numpy as np
import funct
from sys import argv,stderr

script, d_f, l_f = argv

data = funct.Data(d_f, l_f, w0 = False)
labels = data.test_labels
training_data = data.training_rows
#print(labels)

training_data = [data.data[i] for i in training_data]
#print(training_data)
training_labels = [data.labels[i] for i in data.training_rows]
print("\n" + repr(training_labels) + "\n")

test_data = [data.data[i] for i in labels]
print(test_data, out="stderr")

data = np.asarray(training_data)
#print("Original training data")
#print(data)

#print("Original test data")
#print(np.asarray(test_data))

clf = svm.SVC()
clf.fit(data, training_labels)
predictions = clf.predict(np.asarray(test_data))
print(predictions)
