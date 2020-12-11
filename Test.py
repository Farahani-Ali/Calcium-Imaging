#import numpy as np
import pandas as pd
import re

"""
dt = pd.read_csv("./Datasets/F_Plus_Glue.csv")

#dt = dt[dt > 1]
print(dt)
#dt = dt[dt >= 1.2]
def igroups(x):
    s = [0] + [i for i in range(1, len(x)) if x[i] < x[i-1]]  + [len(x)]
    #print(s)
    return [x[j:k] for j, k in [s[i:i+2] for i in range(len(s)-1)] if k - j > 1]


dt['new'] = dt.apply(lambda x : igroups(x),  axis = 1)
print(dt)
"""