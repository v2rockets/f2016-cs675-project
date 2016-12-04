from math import sqrt
from re import split

class Data:
    """Class for data.
    __init__: data file, label file, w0 for linear classifiers
        creates multidimensional list for all data in self.data
        creates dictionary of known labels in self.training_labels
    """

    def __init__(self, data_f, label_f, w0 = False):
        with open(data_f) as f:
            self.data = [[float(datum) for datum in split(r'\s+', line.strip())]
                          for line in f]
        if w0:
            for i in range(len(self.data)):
                self.data[i].append(float(1))

        with open(label_f) as f:
            pass

def gini(c1corr, c2corr, nc1, nc2, nrow)
    """Function to calculate the gini of a split
        args: 
            c1corr: number of items in c1 correctly classified
            c2corr: number of items in c2 correctly classified
            nc1: size of class c1
            nc2: size of class c2
            nrow: size of data overall
    returns gini coefficient of the split
    """
    c1_incorr = nc1 - c1corr
    c2_incorr = nc2 - c2corr
    c1_predict = c1_corr + c2_incorr
    c2_predict = c2_corr + c1_incorr
    if c1_predict == 0: gini1 = 0
    else:
        gini1 = (c1_predict / nrow) * (c1_corr / c1_predict) * \
                (1 - (c1_corr / c1_predict))
    if c2_predict == 0: gini2 = 0
    else:
        gini2 = (c2_predict / nrow) * (c2_corr / c2_predict) * \
                (1 - (c2_corr / c2_predict))
    return gini1 + gini2
