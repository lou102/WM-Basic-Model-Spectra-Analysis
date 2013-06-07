import numpy as np
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
c=2.99e10        #speed of light

ispectra = "85"
filename = "../../Models_Asplund/"+ispectra+"/data/MERGESPEC"

wavelengths,Hnu,continuum,normalspec = np.genfromtxt(filename, dtype="float", unpack=True, skip_header=1, invalid_raise=False, skip_footer=42)


Hlambda = c * Hnu / ( wavelengths * wavelengths)   
Flambda = 4*Hlambda
Fcontinuum = 4*c * continuum / ( wavelengths * wavelengths)   
plt.plot(wavelengths,Flambda, 'k', linewidth=.5, label=r'T$_{\rm eff}$ = 24487'+ '\nlog[g] = 4.060')
plt.plot(wavelengths,Fcontinuum, 'b', label='Continuum')

plt.xlim([0,2000])
plt.xlabel('Wavelength $\AA$', fontsize=15)
plt.ylabel('F$_\lambda$', fontsize=15)
plt.legend(loc="upper right",prop={'size':15})
plt.tick_params(axis='both', which='major', labelsize=15)
plt.savefig('spectra85.ps')
#plt.show()
