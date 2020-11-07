import numpy as np
import pandas as pd
import re


dt = pd.read_csv("./Datasets/F_Plus_Glue.csv")
dt[dt >= 1.2] = 10
dt[dt < 1.2] = 5
dt.astype(str)
dt = dt.replace([10, 5], ['S', 'D'])
dt = dt.sum().reset_index(drop=False)
dt = pd.DataFrame(dt)
dt.rename(columns={0: 'C1'}, inplace=True)

def split_it(mystring):
    return [(m.start(), m.end()) for m in re.finditer('S+', mystring)]

dt['Spikes'] = dt['C1'].apply(split_it)
dt['SpikeCount'] = dt['Spikes'].apply(lambda x: len(x))
## Spikes = Spikes , SpikeCount= SpikeCount

dt.drop(columns=['C1'], inplace=True)


dt["FirstSpike"] = dt["Spikes"].str[0]
dt['FirstSpike'] = (dt['FirstSpike'].str[0]*4)


dt['SpikeLength'] = dt['Spikes'].apply(lambda x: [b-a for a, b in x])
dt['SpikeTimeForEachSpike'] = dt["SpikeLength"].apply(lambda x: [i*4 for i in x])
dt['AverageSpikeTime'] = dt['SpikeTimeForEachSpike'].apply(lambda x : np.mean(x))
dt['SpikeTimeForEachSpike'] = dt['SpikeTimeForEachSpike'].apply(lambda x : [0] if len(x) == 0 else x)
dt['MinSpikeTime'] = dt['SpikeTimeForEachSpike'].apply(lambda x: min(x))
dt['MaxSpikeTime'] = dt['SpikeTimeForEachSpike'].apply(lambda x: max(x))
dt['Sum'] = dt['SpikeTimeForEachSpike'].apply(lambda x: sum(x))
print("averge of average: ", dt['S
print(dt)