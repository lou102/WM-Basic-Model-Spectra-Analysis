import numpy as np
from pylab import *

# define the number of masses in the array and the location of the evol data file
nMass = 20
filename = "../../Data/evol_standard_2solar.dat"


#read in the data from the file
DataIn = np.genfromtxt(filename,dtype="float",unpack=True)

#initially set the index ii
ii=0
#this is for every mass in the array
for imass in range(nMass):

	#initialize the array everytime a new section is found
	massIndiv = []
	
	#set value for the initial mass to an element of the array
	initialMass = DataIn[1,ii]

	#this checks if the row is in the block with the same initial mass
	#if true, it appends that row onto the array, massIndiv
	while DataIn[1,ii] == initialMass:
		row = DataIn[:,ii]
		massIndiv.append(row)
		ii += 1
	
	#these lines determine a filename to be written to, then write
	#the array massIndiv to that file
	directory="../../Data/evol_std_2solar_split/"
	massstring=str(initialMass)
	fileout=directory+"evol_std_2solar_m"+massstring
	np.savetxt(fileout, massIndiv)