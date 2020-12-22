from Dataset import Dataset
from ActiveNueronsDatasetBuilder import ActiveNueronsDatasetBuilder
from Spikes import Spikes


data_set_path = "../Datasets/sample.csv"

dataset = Dataset(data_set_path)
#print(dataset.sequence_status)
active_neron_dataset = ActiveNueronsDatasetBuilder(dataset.sequence_status)


#Spikes(dataSetPath)
