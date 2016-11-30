#!/usr/bin/env python3

from sys import argv
import funct as stat

script, d_f, l_f = argv

data_arr = stat.Data(d_f, l_f, w0 = False)

for i in range(data_arr.cols):
    var_temp = stat.variance(data_arr.get_col(i))
    print("%d %f" % (i, var_temp))
