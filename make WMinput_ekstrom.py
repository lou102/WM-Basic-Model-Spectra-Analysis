import numpy as np
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
griddata=np.genfromtxt(location+'ekstrom_grid.txt', dtype="int", unpack=True)
ii=0
#this is for each mass, read in the file and plot the evolutionary tracks
for imass in range(7):

    filemass = massarr[imass]

    filename = location+fileroot+filemass
    gridpoints=[]
    #print griddata[0,ii],massfloats[imass]
    while griddata[0,ii] == massfloats[imass]:
        gridpoints.append(griddata[1,ii])
        ii += 1

    #read in the data
    DataIn = np.genfromtxt(filename, dtype="float", unpack=True)



    #assign columns of the data to their own variables
    Teff = DataIn[ 7,:]
    L = DataIn[ 6,:]
    M = DataIn[5,:]
    #abundances    
    Hydrogen = [8,:]
    Helium = [9,:]
    C12 = DataIn[ 10,:]
    C13 = DataIn[ 11,:]
    Ctotal = C12+C13
    N14 = DataIn[12,:]
    O16 = DataIn[13,:]
    O17 = DataIn[14,:]
    O18 = DataIn[15,:]
    Ototal = O16+O17+O18
    print C12[0]




    #calculate the surface gravity
    Rsquared=(10**L)*Lsun/(4*math.pi*sigma*(10**Teff)**4)
    R = np.sqrt(Rsquared)/Rsun
    g = M*Msun*Grav/Rsquared
    logg = np.log10(g)





    #plot the tracks and the grid points
    pylab.plot(Teff,L, color='grey', linewidth=2)
    for jj in gridpoints:
        print massarr[imass],jj,M[jj-1],Teff[jj-1],L[jj-1],R[jj-1],logg[jj-1]
        pylab.plot(Teff[jj-1],L[jj-1], 's',color='black', markersize=7)
        


#this is for each mass, read in the file and plot the evolutionary tracks
#for imass in range(24):
#    location = "../../Data/Ekstrom/nonrot/"
#    fileroot = "_ekstrom_"
#    filemass = massarr[imass]
#
#    filename = location+fileroot+filemass
#
#    DataIn = np.genfromtxt(filename, dtype="float", unpack=True)
#
#    Teff = DataIn[ 7,:]
#    L = DataIn[ 6,:]
#
#    pylab.plot(Teff,L, color='blue')
    pylab.xlim([4.9,3.5])
    pylab.ylim([4.5,6.5])

#show all of the tracks that have been plotted
#then save the image
pylab.xlabel(r"Log[T$_{\rm eff}$]", fontsize=20)
pylab.ylabel("Log[L]", fontsize=20)
pylab.title("Evolutionary tracks for rotating solar metalicity stars", fontsize=20)
#saveLoc="../../Images/"
#saveName="Evol_solar.png"
#pylab.savefig(saveLoc+saveName)
pylab.tick_params(axis='both', which='major', labelsize=20)
#pylab.show()

