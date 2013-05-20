import numpy as np
import pylab 
import math


#This is an array of all the masses that are part of the filenames
massarr=['120.0', '85.0', '60.0', '40.0', '25.0', '20.0', '15.0', '12.0', '9.0', '7.0', '5.0', '4.0', '3.0', '2.5', '2.0', '1.7', '1.5', '1.25', '1.0', '0.9']



#this is for each mass, read in the file and plot the evolutionary tracks
for imass in range(20):
	location = "../../Data/evol_std_solar_split/"
	fileroot = "evol_std_solar_m"
	filemass = massarr[imass]

	filename = location+fileroot+filemass

	DataIn = np.genfromtxt(filename, dtype="float", unpack=True)

	Teff = 10**DataIn[ 6,:]
	L = DataIn[ 5,:]

	pylab.plot(Teff,L, color='black')
	pylab.xlim([70000,0])


#show all of the tracks that have been plotted
#then save the image
pylab.xlabel("Teff")
pylab.ylabel("Log[L]")
pylab.title("Evolutionary tracks for solar metalicity stars")
saveLoc="../../Images/"
saveName="Evol_solar.png"
pylab.savefig(saveLoc+saveName)
pylab.show()

