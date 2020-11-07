import numpy as np
import pandas as pd
import re


dt = pd.read_csv("C:/Users/farah/Desktop/Elnaz1/F_Plus_KCL.csv")

#dt = dt.T
#dt = dt[dt > 1]
print(dt)
dt = dt[dt >= 1.2]
def igroups(x):
    s = [0] + [i for i in range(1, len(x)) if x[i] < x[i-1]]  + [len(x)]
    #print(s)
    return [x[j:k] for j, k in [s[i:i+2] for i in range(len(s)-1)] if k - j > 1]



#dt['new'] = dt.apply(lambda x : igroups(x),  axis = 1)
#dt['new1'] = dt["new"].apply(lambda x: len(x))
#print(dt)
dt.to_csv("C:/Users/farah/Desktop/Elnaz1/F_Plus_KCL-new.csv")
#data['SpikeDuration'] = data['SpikeLength'].sum(axis)
#print((list(data.iloc[0, data.columns.get_loc("SpikeLenght")])).sum())