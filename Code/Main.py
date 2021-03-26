from Dataset import Dataset
from ActiveNueronsDatasetBuilder import ActiveNueronsDatasetBuilder
from Spikes import Spikes



#data_set_path = "../Datasets/F_Minus_Glue.csv"
data_set_path = "../Datasets/Broken_Dataset/Fplus_KCIFirst/Fplus_KCIFirst3.csv"


dataset = Dataset(data_set_path)
#active_neron_dataset = ActiveNueronsDatasetBuilder(dataset.sequence_status)
#Spikes(dataset.dt)
ActiveNueronsDatasetBuilder(dataset.sequence_status)

#data_set_path = "../Datasets/spikes.csv"


#dataset = Dataset(data_set_path)
#print(dataset.dt["spikes"])


#Spikes(dataSetPath)
