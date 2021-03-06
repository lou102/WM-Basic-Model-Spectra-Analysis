
#All of my imports
import numpy as np
import pylab
import time
import math
import os
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


#constants (all in cgs)
sigma = 5.67e-5  #stefan-boltzmans constant
G=6.67e-8        #gravitational constant
Msun=1.99e33     #mass of the sun in g
Lsun=3.9e33      #luminosity of the sun
Rsun=6.955e10    #raidius of the sun in cm
h=6.62e-27       #planck's constant
c=2.99e10        #speed of light
k=1.38e-16       #boltzmans constant
nanometer = 1e-7 # conversion from nanometers to centimeters
angstrom = 1e-8  # conversion from angstroms to centimeters
logq0ints = np.zeros(9)


#These are hard coded parameters for the models
#In particular, the radius, temperature, and surface gravity
ModelRs=[12.4, 16.3, 18.4, 20.1, 20.6, 68.7, 59.2, 15.4, 11.3, 14.9, 16.7, 18.6, 21.1, 31.7, 36.9, 14.3, 9.8, 12.9, 
               14.2, 15.9, 18.8, 23.2, 26.2, 58.4, 8.2, 10.8, 11.7, 12.8, 14.3, 16.8, 23.0, 45.1, 7.4, 9.7, 11.3, 13.9,   
               16.4, 22.1, 40.4, 23.5, 6.5, 8.5, 9.7, 11.2, 14.5, 18.5, 29.6, 17.9, 5.7, 7.5, 9.3, 12.0, 14.0, 17.5, 26.1, 75.4,   
               5.0, 6.5, 7.7, 8.5, 9.8, 10.7, 14.3, 18.2, 23.7, 4.4, 5.7, 6.3, 7.3, 9.0, 10.8, 12.3, 17.9, 3.7, 4.9, 5.6, 5.9, 6.2,   
               6.6, 7.0, 9.3, 11.7, 13.7, 3.9, 4.8]
ModelTs=[59870, 52061, 49139, 46967, 46330, 25085, 22339, 25100, 58567, 50928, 48499, 46122, 43501, 35514, 31527, 33117,       
               57000, 49566, 47765, 45683, 42474, 38434, 36653, 24041, 54635, 47509, 46277, 44963, 43138, 40319, 34971,       
               25314, 52465, 45622, 43576, 40507, 37807, 33037, 24880, 29759, 50294, 43734, 42084, 40205, 36500, 32858,       
               26494, 32953, 45971, 39975, 37688, 34549, 32589, 29727, 24838, 15267, 43811, 38097, 36525, 35524, 34052,       
               32982, 29531, 26636, 23768, 40422, 35150, 34298, 33160, 31151, 29320, 27925, 24035, 35864, 31186, 30294,       
               30016, 29660, 29253, 28766, 26393, 24266, 22909, 25453, 24487]
ModelGs=[4.322, 4.078, 3.954, 3.836, 3.761, 2.622, 2.434, 3.017, 4.323, 4.081, 3.972, 3.850, 3.700, 3.277, 3.014, 3.235, 4.352,     
               4.108, 4.016, 3.907, 3.749, 3.512, 3.350, 2.468, 4.383, 4.139, 4.070, 3.985, 3.884, 3.722, 3.428, 2.784,       
               4.393, 4.150, 4.014, 3.824, 3.673, 3.386, 2.817, 2.917, 4.412, 4.170, 4.058, 3.920, 3.678, 3.451, 3.024, 3.122,       
               4.402, 4.159, 3.966, 3.723, 3.584, 3.385, 3.020, 1.872, 4.439, 4.196, 4.056, 3.954, 3.833, 3.744, 3.493,        
               3.266, 3.029, 4.452, 4.209, 4.124, 3.999, 3.804, 3.644, 3.525, 3.195, 4.469, 4.226, 4.113, 4.067, 4.014, 3.969,   
               3.910, 3.665, 3.456, 3.313, 4.237, 4.060]
massarr=np.array([120.0, 85.0, 60.0, 40.0, 25.0, 20.0, 15.0, 12.0, 9.0, 7.0, 5.0, 4.0, 3.0, 2.5, 2.0, 1.7, 1.5, 1.25, 1.0, 0.9])



#plt.figure()






#This is a function that takes in an x, y, and time array, then plots it 
#fading with time.  It does this by splitting up the array into many peices
#then giving each peice a different alpha value
def fadeplot(x, y, time):

    #This normalizes the time array from 0 to 1
    timelastindex = len(time)-1
    timeNormal= time / (time[timelastindex])
    
    #This is the number of elements in the arrays
    length = len(x)    
    

    #This is the algorithm that determines each alpha value based on the time
    alphas = (1-timeNormal)-0.1

    #This checks if any alpha values are negative, and then makes those values 0
    for ii in range(length):
        if alphas[ii] < 0:
            alphas[ii] = 0

    #This is the for loop that plots each segment at a different alpha value
    for iindex in range(length):
        pylab.plot(x[iindex:iindex+2],y[iindex:iindex+2], color='black', alpha=alphas[iindex], linewidth=2)



    #This section will make a color bar, possibly

    #ticks = ( timeNormal ) * 70000
    #ys = np.zeros(length)-0.5
    #for jj in range(length):
    #    pylab.plot(ticks[jj:jj+2],ys[jj:jj+2], color='black', alpha=alphas[jj], linewidth=20)


    return




#This is a function that will read in data of evolutionary tracks, and plot them.
#The input parameters is a mass limit, beyond which the data is not plotted.
def loggtracks(masslimit,location,fileroot, metalstr, plot=True):



    #This is an array of all the masses that are part of the filenames
    massarrstr=['120.0', '85.0', '60.0', '40.0', '25.0', '20.0', '15.0', '12.0', '9.0', '7.0', '5.0', '4.0', '3.0', '2.5', '2.0', '1.7', '1.5', '1.25', '1.0', '0.9']



    #this is for each mass, read in the file and plot the evolutionary tracks
    for imass in range(masslimit):

        filemass = massarrstr[imass]

        filename = location+fileroot+filemass

        DataIn = np.genfromtxt(filename, dtype="float", unpack=True)
    
        time = DataIn[3,:]
        timesec = time*365*24*60*60
        Teff = 10**DataIn[ 6,:]
        logTeff = [math.log10(jj) for jj in Teff]
        L = 10**DataIn[ 5,:]*Lsun
        Rsquared = (L/(4*math.pi*sigma*Teff**4))
        Mass = DataIn[4,:]*Msun
        surfaceGrav = Mass*G/(Rsquared)
        logsurfaceGrav = [math.log10(ii) for ii in surfaceGrav]


        if plot == True:

            fadeplot(Teff, logsurfaceGrav, time)
        
        q0s = np.zeros(len(Teff))
        for timestep in range(len(Teff)):
            q0s[timestep] = interpolate.bisplev(Teff[timestep],logsurfaceGrav[timestep],gridq0s)
            
        
        
        for kk in range(len(q0s)):
            if q0s[kk] < 0:
                q0s[kk] = -q0s[kk]
                q0s[kk] = np.log10(q0s[kk])


        totalQ0s = np.trapz(q0s,timesec)
        
        logtotalQ0s = np.log10(totalQ0s)
        #print "Mass of: " + massarr[imass]+" Produces "+str(totalQ0s)+" Photons"
        logq0ints[imass] = totalQ0s
        #plt.plot(timesec/timesec[-1], q0s, 'k')
        titlestr= "Z= "+metalstr
        #plt.title(titlestr)
        #plt.xlabel("Stellar Lifetime")
        #plt.ylabel("Photons / Second")
        #plt.ylim([0,2e50])
    #plt.show()    
    return;

    


#Decide whether to plot the grid or not
def gridplot(plot=True):
    if plot == True:
        pylab.plot(ModelTs, ModelGs, 'o', color='white', markersize=15)
    






#####################
#
#Main
#
#####################


fig = plt.figure()
for metalicity in range(3):



    Grid = np.array([])
    directories = ["../../Models_Asplund/","../../Models_.5Solar/","../../Models_2Solar/"]  
    location = ["../../Data/evol_std_solar_split/","../../Data/evol_std_.2solar_split/","../../Data/evol_std_2solar_split/"]    
    fileroot = ["evol_std_solar_m","evol_std_.2solar_m","evol_std_2solar_m"]
    metals = ["0.02", "0.004", "0.04"]    

    #This will check the number of models for each metalicity

    model=0
    n_models=84
    #while os.path.isfile(directories[metalicity]+str(model+1)+"/data/MERGESPEC"):
    #    print "The file for model number "+ str(n_models+1)+" exists  "+str(os.path.isfile(directories[metalicity]+str(model+1)+"/data/MERGESPEC"))
    #    n_models=n_models+1
    #    model=model+1

    #print "This would make n_models need to be "+str(n_models)
    
    #directories ="../../Models_Asplund/"
    #location = "../../Data/evol_std_solar_split/"
    #fileroot = "evol_std_solar_m"
    
    for model in range(n_models):
        filename = directories[metalicity]+str(model+1)+"/data/MERGESPEC"

        DataIn = np.genfromtxt(filename, dtype="float", unpack=True, skip_header=1, invalid_raise=False, skip_footer=42)
    
        #Assign values from the data to named arrays
        wavelengths = DataIn[0,:]
        Hnu = DataIn[1,:]
    
        #Change from frequency space to wavelengths space
        Hlambda = c * Hnu / ( wavelengths * wavelengths)   
        Flambda = 4*Hlambda
    
    
        #Integrate the spectra to get the ionizing photon numbers
        lowlimit = 0.
        highlimit = 912
        indices = (wavelengths > lowlimit) & (wavelengths < highlimit)
    
        integrand = math.pi * wavelengths * Flambda / (h*c)
        q0 = -np.trapz(integrand[indices], wavelengths[indices])
        logq0 = math.log10(q0)
        
    
        #Now determine the number of ionizing photons
        radius = ModelRs[model] * Rsun
        photons = 4*math.pi*radius**2*q0
        logphotons = math.log10(photons)
        print "Model #"+str(model)+" has log flux of "+str(logphotons)
        #plt.plot(logphotons)
        #plt.show()
        
        
    
        #This plots the spectra
        #pylab.plot(wavelengths[indices],Flambda[indices])
        #pylab.title("Model number: " +str(model+1))
        #pylab.xlim([0,3000])
        #pylab.show()
    
    
        #This will create the data for the grid, which will then be interpolated
        #Commented out because it is not finished
        newline = [ModelTs[model], ModelGs[model], logphotons]
        Grid=np.append(Grid,newline).reshape(model+1,3)
    
    
    

    #Interpolate the grid of logg vs Teff vs number of ionizing photons
    
    gridq0s = (interpolate.bisplrep(Grid[:,0],Grid[:,1],Grid[:,2]))
    loggtracks(9,location[metalicity],fileroot[metalicity],metals[metalicity],plot=True)
    gridplot(True)
    #plt.show()
    xnew,ynew = np.mgrid[0:70000:200j, -1:5:200j]
    
    znew = interpolate.bisplev(xnew[:,0],ynew[0,:],gridq0s)
    print znew[100,100]
    znew = np.power(10,znew)
    print znew[100,100]

    plt.pcolor(xnew, ynew, np.log10(znew),vmin=46,vmax=52)
    plt.colorbar()
    plt.title("Interpolated Ionizing Photon Fluxes")
    plt.xlabel("Teff")
    plt.ylabel("Log[g]")
    plt.show()
    





  


    



