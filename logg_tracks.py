import numpy as np
import pylab 
import math


#constants
sigma=5.67e-5 #stefan-boltzmans constant
G=6.67e-8     #gravitational constant
Msun=1.99e33  #mass of the sun in g
Lsun=3.9e33   #luminosity of the sun


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
	logTeff = [math.log10(jj) for jj in Teff]
	L = 10**DataIn[ 5,:]*Lsun
	Rsquared = (L/(4*math.pi*sigma*Teff**4))
	Mass = DataIn[4,:]*Msun
	surfaceGrav = Mass*G/(Rsquared)
	logsurfaceGrav = [math.log10(ii) for ii in surfaceGrav]
	pylab.plot(logTeff,logsurfaceGrav, color='black')
	

#show all of the tracks that have been plotted
#then save the image
pylab.xlabel("Log[g]")
pylab.ylabel("Log[Teff]")
pylab.title("Plot of Log[Teff] vs. Log[g] for solar metalicity")
saveLoc="../../Images/"
saveName="surfacegrav_solar.png"
pylab.savefig(saveLoc+saveName)
pylab.show()

