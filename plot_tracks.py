import numpy as np
import matplotlib
matplotlib.use('PS')
import pylab 
import math


#This is an array of all the masses that are part of the filenames
massarr=['120.0', '85.0', '60.0', '40.0', '25.0', '20.0', '15.0', '12.0', '9.0', '7.0', '5.0', '4.0', '3.0', '2.5', '2.0', '1.7', '1.5', '1.25', '1.0', '0.9']

fig=pylab.figure(figsize=(4,10))

#this is for each mass, read in the file and plot the evolutionary tracks
for metalicity in range(3):
    pylab.subplot(3,1,3-metalicity)
    pylab.tight_layout()
    titles=["Z = 0.02",  "Z = 0.004", "Z = 0.04"]
    for imass in range(20):
	    location = ["../../Data/evol_std_solar_split/","../../Data/evol_std_.2solar_split/","../../Data/evol_std_2solar_split/"]
	    fileroot = ["evol_std_solar_m","evol_std_.2solar_m","evol_std_2solar_m"]
	    filemass = massarr[imass]

	    filename = location[metalicity]+fileroot[metalicity]+filemass

	    DataIn = np.genfromtxt(filename, dtype="float", unpack=True)

	    Teff = 10**DataIn[ 6,:]
	    L = DataIn[ 5,:]

	    pylab.plot(Teff/10**4,L, color='black')
	    pylab.xlim([7,0])

    pylab.title(titles[metalicity])
    #show all of the tracks that have been plotted
    #then save the image
    
    pylab.ylabel("Log[L]")
    #pylab.title("Evolutionary tracks for solar metalicity stars")
    if metalicity==0:
        pylab.xlabel(r"T$_{\rm eff}$  [x10$^5$]")
pylab.gcf().subplots_adjust(bottom=0.27)
saveLoc="../../Images/"
saveName="Evol_solar.png"

pylab.savefig("OldTracks.ps")
#pylab.show()

