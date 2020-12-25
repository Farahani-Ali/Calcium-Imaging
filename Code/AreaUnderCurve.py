from __future__ import print_function
import pandas as pd
import numpy as np
from scipy.integrate import simps
from numpy import trapz
from Dataset import Dataset



data_set_path = "../Datasets/sample.csv"

dataset = Dataset(data_set_path)
print(dataset.dt.T)

def area_under_curve (data):
    data = data.T
    areaForFirstRow = simps(data, dx=4)
    print(areaForFirstRow)

dt.dt.apply(area_under_curve(dt.dt))



area_under_curve(dataset.dt)


# Compute the area using the composite trapezoidal rule.
area = trapz([0.98 ,1.20  ,  0.85,  1.19,  1.10], dx=4)
print("area =", area)

# Compute the area using the composite Simpson's rule.
#area = simps(y, dx=4)
#print("area =", area)

