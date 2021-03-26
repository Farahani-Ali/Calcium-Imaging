import pandas as pd
import numpy as np


data = {"row1":[1,2,3,4,5], "row2" : [2,3,4,1,3], "row3":[3,4,2,0,0] }
data = pd.DataFrame(data)
data = data.T
print(data)

def get_row_as_list(indx, data):
    return list(data.iloc[indx,:])



def find_max_in_a_row(row):
    max_value = max(row)
    max_indx = row.index(max_value)
    return max_value, max_indx

def get_sublist_after_max(max_indx, row):
    new_row = row[max_indx:]
    return new_row

def get_min_in_a_row(row):
    min_value = min(row)
    min_indx = row.index(min_value)
    return min_value, min_indx


def calculate_decrease_slope(value_max, indx_min, value_min):
    if indx_min != 0:
        slope = ((value_min) - value_max)/(indx_min)
    else: slope = 0

    return slope

data["decay_slope"] = np.nan

def get_decay_slope_for_all_dataset(data):
    loc = data.columns.get_loc("decay_slope")
    print("loc is", loc)

    for indx in range(len(data)):

        row = get_row_as_list(indx, data)
        print("row is:", row)

        value_max, max_indx = find_max_in_a_row(row)
        print("value max, max indx", value_max, max_indx)

        new_row = get_sublist_after_max(max_indx,row)
        print("new row is", new_row)

        value_min, min_indx = get_min_in_a_row(new_row)
        print("value min, min indx", value_min, min_indx)

        decay_slope = calculate_decrease_slope(value_max,min_indx, value_min)
        print("decay slppe is:", decay_slope)

        data.iloc[indx,loc] = decay_slope
    return data


print(get_decay_slope_for_all_dataset(data))
