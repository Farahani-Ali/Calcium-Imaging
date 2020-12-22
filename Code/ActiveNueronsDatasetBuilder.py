import numpy as np
import pandas as pd
import re

""" 
neuron_status_seq shows a sequence of active/non active statuses for a specific neuron cell, e.g. SSDDS 
shows cell_x was active, active, not_active, not_active, active
"""


class ActiveNueronsDatasetBuilder:
    def __init__(self, sequence_status_dataset):
        self.find_active_periods(sequence_status_dataset)
        self.active_periods_counter(sequence_status_dataset)
        self.drop_first_column(sequence_status_dataset)
        self.find_first_active_time(sequence_status_dataset)
        self.find_activation_length(sequence_status_dataset)
        print(sequence_status_dataset)
        self.find_activation_length_secods(sequence_status_dataset)
        self.find_minimum_active_period(sequence_status_dataset)
        self.find_maximum_active_period(sequence_status_dataset)
        self.sum_of_activat_time_seconds(sequence_status_dataset)
        print(sequence_status_dataset)

        # self.write_to()

    # Finds indices of each active sequence (when a neuron was active (status=S) and when it was not active (status= D))
    def find_active_sequence_indices(self, status, status_sequence):
        return [(m.start(), m.end()) for m in re.finditer(status, status_sequence)]

    def find_active_periods(self, sequence_status_dataset):
        sequence_status_dataset['activePeriods'] = sequence_status_dataset['C1'].apply(
            lambda status_sequence: self.find_active_sequence_indices(status='S+', status_sequence=status_sequence))
        return sequence_status_dataset

    def active_periods_counter(self, active_neurons_dataset):
        active_neurons_dataset['numberOfActivePeriods'] = active_neurons_dataset['activePeriods'].apply(
            lambda x: len(x))
        return active_neurons_dataset

    def drop_first_column(self, active_neurons_dataset):
        active_neurons_dataset.drop(columns=['C1'], inplace=True)
        return active_neurons_dataset

    def find_first_active_time(self, active_neurons_dataset):
        active_neurons_dataset["firstActiveIndex"] = active_neurons_dataset["activePeriods"].str[0]
        active_neurons_dataset['firstActiveTime'] = (active_neurons_dataset['firstActiveIndex'].str[0] * 4)
        return active_neurons_dataset

    def find_activation_length(self, active_neurons_dataset):
        active_neurons_dataset['activationLength'] = active_neurons_dataset['activePeriods'].apply(
            lambda x: [b - a for a, b in x])
        active_neurons_dataset['activationLength'] = active_neurons_dataset['activationLength'].apply(
            lambda x: [0] if len(x) == 0 else x)
        return active_neurons_dataset

    def find_activation_length_secods(self, active_neurons_dataset):
        active_neurons_dataset['activationTimeInSeconds'] = active_neurons_dataset["activationLength"].apply(
            lambda x: [i * 4 for i in x])
        return active_neurons_dataset

    def find_minimum_active_period(self, active_neurons_dataset):
        active_neurons_dataset['minActiveTimeInSecdons'] = active_neurons_dataset['activationTimeInSeconds'].apply(
            lambda x: min(x))
        return active_neurons_dataset

    def find_maximum_active_period(self, active_neurons_dataset):
        active_neurons_dataset['maxActiveTimeInSeconds'] = active_neurons_dataset['activationTimeInSeconds'].apply(
            lambda x: max(x))
        return active_neurons_dataset

    def sum_of_activat_time_seconds(self, active_neurons_dataset):
        active_neurons_dataset['sumOfActiveTimeInSeconds'] = active_neurons_dataset['activationTimeInSeconds'].apply(
            lambda x: sum(x))
        return active_neurons_dataset

