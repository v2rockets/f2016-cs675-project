#!/usr/bin/env python2

from __future__ import print_function
import numpy as np
import funct
from sys import argv

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA
from sklearn import svm

script, d_f, l_f, filename = argv

data = funct.Data(d_f, l_f, w0 = False)
labels = data.test_labels
training_data = data.training_rows

training_data = [data.data[i] for i in training_data]
training_labels = [data.labels[i] for i in data.training_rows]

test_data = [data.data[i] for i in labels]

print("\nWorking with %s, out file prefix %s" % (l_f, filename))
data = np.asarray(training_data)
print("Data shape overall: ", data.shape)

clf = ExtraTreesClassifier()
clf = clf.fit(data, training_labels)
important_features = filename + ".important_features"
with open(important_features, "w") as f:
    for i in range(len(clf.feature_importances_)):
        f.write("%d\t%f\n" % (i, clf.feature_importances_[i]))

model = SelectFromModel(clf, prefit = True)
data_new = model.transform(data)
print("New data shape: ", data_new.shape)

print()

test_data = model.transform(test_data)

svm_clf = svm.SVC()
svm_clf.fit(data_new, training_labels)
predictions = svm_clf.predict(test_data)
with open(filename + ".predict", "w") as f:
    for i in range(len(labels)):
        f.write("%d %d\n" % (labels[i], predictions[i]))
