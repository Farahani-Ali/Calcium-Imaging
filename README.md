# Calcium-Imaging

The goal of this project is to find active time and spikes of neuron cells which are treated by positive and negative Glutamine or KCL. 

A neron cell is defined active if the cell's brightness is equal or above 1.2. 

## Dataset class 

In this class, we read the dataset and drop the "time column", then we replace any cell which has a value greater than an equal to 1.2 with "S" and any value bellow 1.2 with "D"

