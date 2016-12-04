from sys import argv
import funct as stat

script, df, lf = argv

data_arr = stat.Data(df, lf, w0 = False)

for j in range(data_arr.cols):
    
