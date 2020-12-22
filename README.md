# Calcium-Imaging

The goal of this project is to find active time and spikes of neuron cells which are treated by positive and negative Glutamine or KCL. 

A neron cell is defined active if the cell's brightness is equal or above 1.2. 

## Dataset class 

In this class, we do the following steps
* read the dataset
* drop the "time column"
* replace any value which is greater than or equal to 1.2 with "S" and any value bellow 1.2 with "D"
* create a list of S/D for each neuron cell using regular expression, we will use this list to find periods that a cell was active 

## ActiveNuerondatasetBuilder class 

In this class we do the following step
* using the S/D sequence for each neuron cell, we find periods that a cell was active/non-active
* count the numebr of times a cell was active 
* drops the sequence S/D sequence 
* Finds the time when a cell became active for the first time
* finds the duration (in seconds) for each period of activation 
* finds average of time a neuron was active
* gives the minimum and maximum periods of activation for a neuron cell 


## Spike class

Spike is defined as any "non-decreasing" sequence of values (of a neuron's brighness) that meets two following requirements:
1. difference of the highest and lowest number of sequence is greater or equal to .1
2. the highest number is greater than 1.2
