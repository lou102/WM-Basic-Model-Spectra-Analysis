#All of my imports
import numpy as np
import matplotlib
##matplotlib.use('PS')
import time
import math
import os
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


#This section will ask the user what to do
#The options are plotting a figure of lifetime integrated Q0 production vs. initial mass or
#plotting total ionizing photon production vs total mass of a population
plotQ0 = False
imfAdjust = False

print "What would you like to do?\n"
print "(1) Plot lifetime integrated Q0 vs. Initial mass.\n"
print "(2) Plot total ionizing photons integrated over an IMF.\n"

decision = input("(1 or 2)? ")
if decision == 1:
    plotQ0 = True
    print "This is happening, right?"
elif decision == 2:
    imfAdjust = True
else:
    print "You chose wrong, try again."




start=time.time()

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
beta = -2.5
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





#This is a function that will read in data of evolutionary tracks, and plot them.
#It also will interpolate the lifetime Q0 production along a track
#The input parameters is a mass limit, beyond which the data is not plotted.
def loggtracks(masslimit,location,fileroot, metalstr, plot=True):

    #This is an array of all the masses that are part of the filenames
    massarrstr=['120.0', '85.0', '60.0', '40.0', '25.0', '20.0', '15.0', '12.0', '9.0', '7.0', '5.0', '4.0', '3.0', '2.5', '2.0', '1.7', '1.5', '1.25', '1.0', '0.9']

    #this is for each mass, read in the file and plot the evolutionary tracks
    for imass in range(masslimit):
        print "Using mass: "+str(massarrstr[imass])
        #Producing the location of the file
        print "Reading in evolutionary track data."
        filemass = massarrstr[imass]
        filename = location+fileroot+filemass

        #Read in the data
        DataIn = np.genfromtxt(filename, dtype="float", unpack=True)
    
        #Set the variables from the "DataIn" array to more meaningful terms, then use them to calculate some basic paramaters
        time = DataIn[3,:]
        timesec = time*365*24*60*60
        Teff = 10**DataIn[ 6,:]
        logTeff = [math.log10(jj) for jj in Teff]
        L = 10**DataIn[ 5,:]*Lsun
        Rsquared = (L/(4*math.pi*sigma*Teff**4))
        Mass = DataIn[4,:]*Msun
        surfaceGrav = Mass*G/(Rsquared)
        logsurfaceGrav = [math.log10(ii) for ii in surfaceGrav]

        #Create the q0s array then fill it along the evolutionary track from the interpolated grid  
        print "Interpolating the time snapshot on the grid."      
        q0s = np.zeros(len(Teff))
        for timestep in range(len(Teff)):
            q0s[timestep] = np.power(10,interpolate.bisplev(Teff[timestep],logsurfaceGrav[timestep],gridq0s))
            
            
        #For some reason, some values are negative, this fixes that
        for kk in range(len(q0s)):
            if q0s[kk] < 0:
                q0s[kk] = -q0s[kk]
                q0s[kk] = np.log10(q0s[kk])

        #This is the integration of the integrated Q0.  It then takes the log of it and sets the value to an array.
        print "Integrating the Q0 production over a lifetime."
        totalQ0s = np.trapz(q0s,timesec)
        logtotalQ0s = np.log10(totalQ0s)
        logq0ints[imass] = totalQ0s
  
    return;

    


#Decide whether to plot the grid or not
def gridplot(plot=True):
    print "Plotting the grid."
    if plot == True:
        plt.plot(ModelTs, ModelGs, '+', color='blue', markersize=10)
    


#Function IMFconst
#  takes arguments of:
#  totalmass:   total mass of a population
#It is given a total mass and integrates an IMF from Kroupa 2001 to find the normalization constant
#it then returns that value
def IMFconst():

    masstot = []
    imftot = []
    masslow = np.arange(0.01, 0.08, 0.01)
    massmed = np.arange(0.08, 0.5, 0.01)
    masshigh = np.arange(0.5, 120.5, 0.5)
    imflow = masslow ** (-0.3+1)
    imfmed = massmed ** (-1.3+1)
    imfhigh = masshigh ** (beta+1)
    masstot = np.append(masstot, np.append(masslow, np.append(massmed, masshigh)))
    imftot = np.append(imftot, np.append(imflow, np.append(imfmed, imfhigh)))
    
    integratedmass = np.trapz(imftot, masstot, 0.01)


    return integratedmass  




#function imfMultiply
#  takes arguments of:
#  massarr:    initial mass array
#  logq0ints:  lifetime integrated Q0 for each initial mass
#  C:          normalization constant
#The function multiplies the array logq0ints by an imf then integrates it and returns that value
#The integral is negative because the massarr is in decending order
def imfMultiply(massarr, logq0ints):  
    IMF = massarr[0:6] ** beta
    QofMtot = -np.trapz(IMF * logq0ints[0:6], massarr[0:6], 1)
    return QofMtot
    
    



#####################
#
#Main
#
#####################


print "__MAIN__"
#Create a figure
fig = plt.figure()

for metalicity in range(3):
    #This block defines the blank array "Grid" that will later be used in the interpolation
    #Also define the different locations for the data for each metalicity
    Grid = np.array([])
    directories = ["../../Models_Asplund/","../../Models_.5Solar/","../../Models_2Solar/"]  
    location = ["../../Data/evol_std_solar_split/","../../Data/evol_std_.2solar_split/","../../Data/evol_std_2solar_split/"]    
    fileroot = ["evol_std_solar_m","evol_std_.2solar_m","evol_std_2solar_m"]
    metals = ["0.02", "0.004", "0.04"]    
    print "Starting calculation with metalicity: "+str(metals[metalicity])
    #This will check the number of models for each metalicity
    #It is currently not being used but may be useful if you run your own grid
    model=0
    n_models=0
    while os.path.isfile(directories[metalicity]+str(model+1)+"/data/MERGESPEC"):
        n_models=n_models+1
        model=model+1
    

    print "Reading in model spectra and integrating."
    for model in range(n_models):
        #The filename for the spectrum
        filename = directories[metalicity]+str(model+1)+"/data/MERGESPEC"

        #Read in the file that contains the simulated spectral data
        DataIn = np.genfromtxt(filename, dtype="float", unpack=True, skip_header=1, invalid_raise=False, skip_footer=42)
    
        #Assign values from the data to named arrays
        wavelengths = DataIn[0,:]
        Hnu = DataIn[1,:]
    
        #Change from frequency space to wavelengths space
        Hlambda = c * Hnu / ( wavelengths * wavelengths)   
        Flambda = 4*Hlambda
    
        #Integrate the spectra to get the ionizing photon numbers
        #the Highlimit value can be changed to easily pick a different continuum, HeII for example
        lowlimit = 0.
        highlimit = 912.
        indices = (wavelengths > lowlimit) & (wavelengths < highlimit)
        integrand = math.pi * wavelengths * Flambda / (h*c)
        q0 = -np.trapz(integrand[indices], wavelengths[indices])
        logq0 = math.log10(q0)
    
    
        #Now determine the number of ionizing photons
        radius = ModelRs[model] * Rsun
        photons = 4*math.pi*radius**2*q0
        logphotons = math.log10(photons)
               
        #This will create the data for the grid, which will then be interpolated
        newline = [ModelTs[model], ModelGs[model], logphotons]
        Grid=np.append(Grid,newline).reshape(model+1,3)
 

    #This is the interpolation function for the grid
    print "Interpolating the spectra on a grid."
    gridq0s = (interpolate.bisplrep(Grid[:,0],Grid[:,1],Grid[:,2]))
    loggtracks(9,location[metalicity],fileroot[metalicity],metals[metalicity],plot=False)
    #Plot the grid of points?
    gridplot(False)
    #Define the x and y coords of the interpolated array
    xnew,ynew = np.mgrid[0:70000:200j, -1:5:200j]
    #Make the final 2D array that has our interpolated data in it
    znew = interpolate.bisplev(xnew[:,0],ynew[0,:],gridq0s)
    #Bring the data out of log space
    znew = np.power(10,znew)

    
    #This creates a least squares regression fit to the data
    print "Making a linear fit to the data."
    A = np.vstack([massarr[1:6], np.ones(5)]).T
    m, c = np.linalg.lstsq(A, logq0ints[1:6]/(1e63))[0]
    x = massarr[0:6]
    y = [((m * ii) + c) for ii in x]

    #Define different symbols and titles for each metalticity
    "Plotting the data."
    psym=['k^','bo','rs']
    metals=['0.02','0.004','0.04']
    label='Z = '+metals[metalicity]
    #Define the different lines to be plotted for each metalicity
    linestyle=['k-','b--','r:']


    #if the user chose to plot lifetime integrated Q0 vs initial mass
    if plotQ0 == True:
        #Plot the data points with different symbols and colors
        plt.plot(massarr[0:6], logq0ints[0:6]/(1e63), psym[metalicity], markersize=6,label=label)


        #Two different lines to plot.  The first is a line connecting the data,
        #  and the second is a linear fit to the data
        plt.plot(massarr[0:6], logq0ints[0:6]/(1e63), linestyle[metalicity], linewidth=1.5)
        #plt.plot(massarr[0:6], m*massarr[0:6]+c,  linestyle[metalicity], linewidth=3,label=label)
    


    #This will multiply the Q0 function by an imf and integrate it, if the user chose to
    if imfAdjust == True:
        #This is a blank array initialization
        #This is the range of total masses
        #for each total mass of a population
        integratedmass = IMFconst()
        #this calls the procedure IMFconst, which takes args of a total mass and returns a value for the normalization const
            #This line calls the function imfMultiply which takes args of the initial mass array, the lifetime integrated
            #  photon fluxes, and the normalization constant.  It returns the total ionizing flux for a population
            #  with that mass
        QofTotalMass = imfMultiply(massarr, logq0ints)
        #This plots the functions on a log plot
       # plt.plot(np.log10(totalMasses), (QofTotalMass), linestyle[metalicity], linewidth = 3, label=label)
        print "For metalicity of Z="+str(metals[metalicity])+"The ionizing photons per solar mass are: "+str(QofTotalMass/integratedmass)



#This makes the plot
print "Showing the data."
if imfAdjust == True:
    print "imfAdjust is True"
    plt.legend(loc="upper left",prop={'size':15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.xlabel(r"Log$[\rm M_{\rm tot}$]", fontsize=15)
    plt.ylabel("Total $Q_0$", fontsize=15)
    #plt.savefig('IMFLifeIntegratedQ0.ps')

if plotQ0 == True:
    plt.legend(loc="upper left",prop={'size':15})
    plt.gcf().subplots_adjust(bottom=0.17)
    plt.xlim([15,125])
    plt.ylim([0,8])
    plt.xlabel(r"Initial Mass  (M$_\odot$)",fontsize=15)
    plt.ylabel(r"Lifetime Integrated $Q_0$  [1e63]",fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    #plt.savefig('LifeIntegratedQ0.ps')

#Show the figure
print "This program took: "+str(time.time()-start) + " to run"
plt.show()


