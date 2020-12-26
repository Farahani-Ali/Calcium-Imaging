from __future__ import print_function
import pandas as pd
import numpy as np
from scipy.integrate import simps
from numpy import trapz
from Dataset import Dataset



data_set_path = "../Datasets/sample.csv"
dataset = Dataset(data_set_path)
dt = dataset.dt.T

dt = dt.applymap(lambda x: x-1)
print(dt)
dt['list_of_all_values'] = dt.agg(list, axis=1)

def area_under_curve_calculator(curve_values, time_step):
    area_under_curve = simps(curve_values, dx = time_step)
    return area_under_curve

dt["are_under_curve"] = dt["list_of_all_values"].apply(lambda x: area_under_curve_calculator(x, time_step= 4))
print(dt)

