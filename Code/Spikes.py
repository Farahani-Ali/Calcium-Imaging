import numpy as np
import pandas as pd
import re
import functools
import itertools


class Spikes:

    def __init__(self, dataset):
        self.dt = dataset.T
        #self.dt['IncreasingSequences'] = self.dt.agg(list, axis=1)
        self.dt['IncreasingSequences'] = self.dt.apply(lambda x: self.non_decreasing_sequence_for_row(x), axis=1)
        # print(self.dt)
        self.dt["spikes"] = self.dt["IncreasingSequences"].apply(self.spike_finder)
        self.spike_counter()
        self.dt["spikeSlope"] = self.dt["spikes"].apply(self.slope_collector)
        print(self.dt)
        self.save_to_csv()
        #self.save_to_jason()

        # self.dt['NumberOfIncreasingSequences'] = self.dt["IncreasingSequences"].apply(lambda x: len(x))

        # self.dt['SpikeDuration'] = self.dt['SpikeLength'].sum(axis=1)

    # https://stackoverflow.com/questions/33402355/finding-groups-of-increasing-numbers-in-a-list/33403822
    def non_decreasing_sequence_for_row(self, row):
        # find the indices where numbers are non decreasing
        indices = [i for i in range(1, len(row)) if row[i] < row[i - 1]]
        # add the start and end indices
        indices = [0] + indices + [len(row)]
        # take the indices as pairwise slices
        slices = [indices[i:i + 2] for i in range(len(indices) - 1)]
        # extract all sequences with length greater than one
        non_decreasing_values = [row[start:end] for start, end in slices if end - start > 1]
        return non_decreasing_values

# filters the increasing sequences to see if a sequence is spike or not
    def filter_spike(self, increasing_sequence):
        mi, *_, ma = increasing_sequence
        return ma > 1.2 and ma - mi > 0.1

    def spike_finder(self, increasing_sequences):
        return [lst for lst in increasing_sequences if self.filter_spike(lst)]

    def slope_of_first_pick(self):
        self.dt['slope'] = self.dt["IncreasingSequences"]

    def get_slope_for_a_spike(self, spike):
        min, *_, max = spike
        max_min_difference = max - min
        time = len(spike)-1  # -1 is because we want the time between first and last element
        slope = max_min_difference / (time * 4)
        return slope

    def slope_collector(self, increasing_sequences):
        slopes = [self.get_slope_for_a_spike(lst) for lst in increasing_sequences]
        if len(slopes) > 0:
            return slopes[0]

    def spike_counter(self):
        self.dt["spikeCounts"] = self.dt['spikes'].apply(lambda x: len(x))

        # return increasing_sequences

    def save_to_csv(self):
        self.dt.to_csv("../Datasets/Spikes.csv")

    def save_to_jason(self):
        self.dt['spikes'].to_json( "../Datasets/Spikes.json")
        #self.dt['IncreasingSequences'].to_json( "../Datasets/Spikes.json")