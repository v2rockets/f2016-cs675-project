#!/usr/bin/env python3

from re import split
from math import sqrt

class Data:
    """Class for data, including methods of getting rows."""

    def __init__(self, data_f, label_f, w0 = True):
        """Importing data"""
        with open(data_f) as f:
            self.data = [[float(datum) for datum in split(r'\s+', line.strip())] for line in f]
        if w0:
            for i in range(len(self.data)):
                self.data[i].append(float(1))
        else: pass
        with open(label_f) as f:
            self.labels = {int(row):int(label) for label,row in [split(r'\s+', line.strip()) for line in f]}
        self.test_labels = list(set(range(len(self.data))) - set(self.labels.keys()))
        self.test_labels.sort()
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        self.n_case = len([0 for x in self.labels.values() if x == 1])
        self.n_control = self.rows - self.n_case

    def get_col(self, col_i):
        return [row[col_i] for row in self.data]
    def get_row(self, row_i):
        return self.data[row_i]
    def get_label(self, row_i):
        if row_i in self.labels: return self.labels[row_i]
        else:
            print("Label does not exist: is this a test label?")
            return

def dot_product(vect1, vect2):
    if len(vect1) != len(vect2):
        raise ValueError("Invalid operation, differing vector lengths")
    return sum([vect1[i] * vect2[i] for i in range(len(vect1))])

def mean(vect):
    return sum(vect) / len(vect)

def variance(vect):
    vect_mean = mean(vect)
    return sum([(vect[i] - vect_mean) ** 2 for i in range(len(vect))]) / len(vect)

def std_dev(vect):
    return sqrt(variance(vect))
