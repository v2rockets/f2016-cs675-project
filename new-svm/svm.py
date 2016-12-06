#!/usr/bin/env python2

from __future__ import print_function
import numpy as np
import funct
from sys import argv
from sklearn import svm

if len(argv) != 4:
    print("""Please run in format
    script data_file labels_file out_file""")
    quit()
script, d_f, l_f, filename = argv

data = funct.Data(d_f, l_f, w0 = False)
labels = data.test_labels
training_data = data.training_rows

training_data = [data.data[i] for i in training_data]
training_labels = [data.labels[i] for i in data.training_rows]

test_data = [data.data[i] for i in labels]

print("\nWorking with %s, out file prefix %s" % (l_f, filename))
data = np.asarray(training_data)

svm_clf = svm.LinearSVC()
svm_clf.fit(data, training_labels)
predictions = svm_clf.predict(test_data)
with open(filename + ".predict", "w") as f:
    for i in range(len(labels)):
        f.write("%d %d\n" % (predictions[i], labels[i]))
print("Data shape overall: ", data.shape)
