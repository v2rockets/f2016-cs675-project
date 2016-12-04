#!/usr/bin/env python2

from __future__ import print_function
import numpy as np
import funct
from sys import argv

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA

script, d_f, l_f, filename = argv

data = funct.Data(d_f, l_f, w0 = False)
labels = data.test_labels
training_data = data.training_rows

training_data = [data.data[i] for i in training_data]
training_labels = [data.labels[i] for i in data.training_rows]

print("Working with %s, out file prefix %s" % (l_f, filename))
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

### Doing PCA in order to visualize what the data looks like after the feature selection, it's easier ###

pca = PCA(n_components = 2)
pca.fit(data_new)
data_applied = pca.transform(data_new)

with open(filename + ".results", "w") as f:
    for i in range(len(training_data)):
        f.write("%d %f %f\n" % (training_labels[i], data_applied[i][0], data_applied[i][1]))

print()
