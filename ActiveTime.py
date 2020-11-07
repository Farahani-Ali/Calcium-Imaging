import numpy as np
import pandas as pd
import re


class ActiveTime:
    def __init__(self, dataSetPath):
        self.dt = pd.read_csv(dataSetPath)
        # self.dt = self.dt.iloc[:, 1:]  # Drops the time column
        self.replace_numbers_with_letters()
        self.combine_letters_for_a_cell()
        print(self.dt)
        self.finding_active_times()
        self.write_to()

    def replace_numbers_with_letters(self):
        self.dt[self.dt >= 1.2] = 10
        self.dt[self.dt < 1.2] = 5
        self.dt.astype(str)
        self.dt = self.dt.replace([10, 5], ['S', 'D'])

    def combine_letters_for_a_cell(self):
        self.dt = self.dt.sum().reset_index(drop=False)
        self.dt = pd.DataFrame(self.dt)
        self.dt.rename(columns={0: 'C1'}, inplace=True)

    def reg_exp_for_s_sequences(self):
        return [(m.start(), m.end()) for m in re.finditer('S+', self.dt)]

    def finding_active_times(self):
        self.dt['Spikes'] = self.dt['C1'].apply(self.reg_exp_for_s_sequences())
        self.dt['SpikeCount'] = self.dt['Spikes'].apply(lambda x: len(x))
        self.dt.drop(columns=['C1'], inplace=True)

        self.dt["FirstSpike"] = self.dt["Spikes"].str[0]
        self.dt['FirstSpike'] = (self.dt['FirstSpike'].str[0] * 4)

        self.dt['SpikeLength'] = self.dt['Spikes'].apply(lambda x: [b - a for a, b in x])
        self.dt['SpikeTimeForEachSpike'] = self.dt["SpikeLength"].apply(lambda x: [i * 4 for i in x])
        self.dt['AverageSpikeTime'] = self.dt['SpikeTimeForEachSpike'].apply(lambda x: np.mean(x))
        self.dt['SpikeTimeForEachSpike'] = self.dt['SpikeTimeForEachSpike'].apply(lambda x: [0] if len(x) == 0 else x)
        self.dt['MinSpikeTime'] = self.dt['SpikeTimeForEachSpike'].apply(lambda x: min(x))
        self.dt['MaxSpikeTime'] = self.dt['SpikeTimeForEachSpike'].apply(lambda x: max(x))
        self.dt['Sum'] = self.dt['SpikeTimeForEachSpike'].apply(lambda x: sum(x))

    def write_to(self):
        self.dt.to_csv("./Datasets/ActiveTime.csv")
