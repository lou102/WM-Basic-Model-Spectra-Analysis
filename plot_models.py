#All of my imports
import numpy as np
import pylab
import time
import math
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
		
	
	return;

	

		








#####################
#
#Main
#
#####################





for metalicity in range(3):
    
	fig=plt.figure()
	n_models = 84
	plt.plot(ModelTs, ModelGs, 'k+', markersize=10)
	Grid = np.array([])
	directories = ["../../Models_Asplund/","../../Models_.5Solar/","../../Models_2Solar/"]
	location = ["../../Data/evol_std_solar_split/","../../Data/evol_std_.2solar_split/","../../Data/evol_std_2solar_split/"]
	fileroot = ["evol_std_solar_m","evol_std_.2solar_m","evol_std_2solar_m"]
	metals = ["0.02", "0.004", "0.04"]	
	loggtracks(7,location[metalicity],fileroot[metalicity],metals[metalicity],True)
	

	plt.title("$Z="+metals[metalicity]+"$",fontsize=30)
	plt.xlabel("$T_{eff}$",fontsize=20)
	plt.ylabel("$Log[g]$",fontsize=20)
	plt.xlim([10000,65000])
	plt.ylim([0,5])
	plt.draw()
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	plt.tick_params(axis='both', which='major', labelsize=20)
	

plt.show()

























