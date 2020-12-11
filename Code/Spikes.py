import numpy as np
import pandas as pd
import re


class Spikes:

    def __init__(self, dataSetPath):
        self.dt = pd.read_csv(dataSetPath)
        self.dt = self.dt.T
        self.dt['IncreasingSequences'] = self.dt.apply(lambda x: self.find_all_increasing_sequences(), axis=1)

        # self.dt['NumberOfIncreasingSequences'] = self.dt["IncreasingSequences"].apply(lambda x: len(x))
        # self.dt['SpikeDuration'] = self.dt['SpikeLength'].sum(axis=1)

    def find_all_increasing_sequences(self):
        nonDecrsngSequences = [0] + [i for i in range(1, len(self.dt)) if self.dt[i] < self.dt[i - 1]] + [
            len(self.dt)]
        return [self.dt[j:k] for j, k in [nonDecrsngSequences[i:i + 2] for i in range(len(nonDecrsngSequences) - 1)] if
                k - j > 1]

    def write_To(self):
        self.dt.to_csv("./Datasets/Spikes.csv")
