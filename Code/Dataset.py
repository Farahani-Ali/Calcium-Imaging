import pandas as pd
import numpy as np


class Dataset:
    def __init__(self, dataSetPath):
        self.dt = pd.read_csv(dataSetPath)
        self.dt = self.dt.iloc[:, 1:]  # Drops the time column
        self.sequence_status = self.find_status_of_cells(activation_threshold=1.2)
        self.sequence_status = self.give_sequence_status(self.sequence_status)

    # Finds status of each cell for each time, when it is more than activation threshold the status is (spike = S) and
    # when the value of the cell is bellow the threshold the status is (Dark = D)
    def find_status_of_cells(self, activation_threshold):
        return pd.DataFrame(np.where(self.dt >= activation_threshold, 'S', 'D'))

    # Gives sequences of statuses (S or D) of each cell
    def give_sequence_status(self, sequence_status):
        sequence_status = sequence_status.sum().reset_index(drop=False)
        sequence_status = pd.DataFrame(sequence_status)
        sequence_status.rename(columns={0: 'C1'}, inplace=True)
        return sequence_status
