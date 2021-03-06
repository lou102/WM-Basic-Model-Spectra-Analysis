import numpy as np
import matplotlib
matplotlib.use('PS')
import pylab 
import math


sigma=5.67e-5
Lsun = 3.9e33
Rsun = 6.96e10
Msun = 1.99e33
Grav = 6.67e-8
location = "../../Data/Ekstrom/rot/"
    
fileroot = "_ekstrom_"
#This is an array of all the masses that are part of the filenames
massarr=['120.', '85.', '60.', '40.', '32.', '25.', '20.', '15.', '12.', '9.', '7.', '5.', '4.', '3.', '2.5', '2.0', '1.7', '1.5', '1.35', '1.25', '1.1', '1.0', '0.9', '0.8']
massfloats=[120,85,60,40,32,25,20]
#gridpoints=[1,85,111,192,209,368,393]

ii=0
#this is for each mass, read in the file and plot the evolutionary tracks
for imass in range(7):

    filemass = massarr[imass]

    filename = location+fileroot+filemass



    DataIn = np.genfromtxt(filename, dtype="float", unpack=True)

    Teff = DataIn[ 7,:]
    L = DataIn[ 6,:]
    M = DataIn[5,:]
    Rsquared=(10**L)*Lsun/(4*math.pi*sigma*(10**Teff)**4)
    R = np.sqrt(Rsquared)/Rsun
    g = M*Msun*Grav/Rsquared
    logg = np.log10(g)
    if imass == 0:
        pylab.plot(Teff,L,'k', label='Rot')
    pylab.plot(Teff,L,'k')


#this is for each mass, read in the file and plot the evolutionary tracks
for imass in range(7):
    location = "../../Data/Ekstrom/nonrot/"
    fileroot = "_ekstrom_"
    filemass = massarr[imass]

    filename = location+fileroot+filemass

    DataIn = np.genfromtxt(filename, dtype="float", unpack=True)

    Teff = DataIn[ 7,:]
    L = DataIn[ 6,:]
    if imass == 0:
        pylab.plot(Teff,L, color='blue', label='Nonrot')
    pylab.plot(Teff,L, color='blue')
    pylab.xlim([4.9,3.5])
    pylab.ylim([4.5,6.53])

#show all of the tracks that have been plotted
#then save the image
pylab.xlabel(r"Log[T$_{\rm eff}$]", fontsize=15)
pylab.ylabel("Log[L]", fontsize=15)
#pylab.title("Evolutionary tracks for rotating stars (Z = 0.014)", fontsize=20)
#saveLoc="../../Images/"
#saveName="Evol_solar.png"
#pylab.savefig(saveLoc+saveName)
pylab.gcf().subplots_adjust(bottom=0.17)
pylab.tick_params(axis='both', which='major', labelsize=15)
pylab.legend(loc="lower left",prop={'size':15})
pylab.savefig('EkstromTracksHighMass.ps')
pylab.show()

