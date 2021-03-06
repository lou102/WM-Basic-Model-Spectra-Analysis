import numpy as np
from pylab import *

# define the number of masses in the array and the location of the evol data file
nMass = 48
filename = "../../Data/Ekstrom/tables.dat"


#read in the data from the file
DataIn = np.genfromtxt(filename,dtype="string",unpack=True)

#initially set the index ii
ii=0
#this is for every mass in the array
for imass in range(nMass):
    kk=0
    #initialize the array everytime a new section is found
    massIndiv = []
    
    #set value for the initial mass to an element of the array
    initialMass = DataIn[0,ii]

    #this checks if the row is in the block with the same initial mass
    #if true, it appends that row onto the array, massIndiv
    while kk < 400:
        row = DataIn[:,ii]
        massIndiv.append(row)
        ii=ii+1
        kk=kk+1


    switch=(-1)**imass
    #these lines determine a filename to be written to, then write
    #the array massIndiv to that file
    print switch
    if switch == 1:
        directory="../../Data/Ekstrom/nonrot/"
        massstring=str(initialMass)
        fileout=directory+"_ekstrom_"+massstring
        np.savetxt(fileout, massIndiv,fmt='%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s ')
    else:
        directory="../../Data/Ekstrom/rot/"
        massstring=str(initialMass)
        fileout=directory+"_ekstrom_"+massstring
        np.savetxt(fileout, massIndiv,fmt='%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s ')


