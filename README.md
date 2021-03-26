# Calcium-Imaging

This project aims to analyse data of reaction of neruons which are treated with Glutamine and KCL with positive and negative conditions. This Proejct was funded through NSF (National Science Foundation). 


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

## AreaUnderCurve class

Finds the area under curve and above brighness of 1. Bellow line 1 a cell is considered as dead so we ignore anything bellow that. 

## Slope class

finds the slope between the cell before treatment and the pick afterwards 
