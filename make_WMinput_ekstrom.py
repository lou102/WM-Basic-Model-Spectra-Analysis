import numpy as np
import pylab 
import math
import os
import LFParameters


sigma=5.67e-5
Lsun = 3.9e33
Rsun = 6.96e10
Msun = 1.99e33
Grav = 6.67e-8
modelloc = "../../Models_Ekstrom/"
location = "../../Data/Ekstrom/rot/"
model=0
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
    Hydrogen = DataIn[8,:]
    
    Helium = DataIn[9,:]
    #helium total is the number fraction of helium to hydrogen
    Hetotal = (Helium/4.)
    Hetotalnorm = (Helium/4.)/Hydrogen
    C12 = DataIn[ 10,:]
    C13 = DataIn[ 11,:]
    #ctotal is the number fraction of carbon to hydrogen
    Ctotal = (C12/12.+C13/13.)
    Ctotalnorm = (C12/12.+C13/13.)/Hydrogen
    N14 = DataIn[12,:]
    #Ntotal is the number fraction of nitrogen to hydrogen
    Ntotal = (N14/14.)
    Ntotalnorm = (N14/14.)/Hydrogen
    O16 = DataIn[13,:]
    O17 = DataIn[14,:]
    O18 = DataIn[15,:]
    #Ototal is the number fraction of oxygen to hydrogen
    Ototal = (O16/16.+O17/17.+O18/18.)
    Ototalnorm = (O16/16.+O17/17.+O18/18.)/Hydrogen

    #print Hetotal[0]/(.1),Ctotal[0]/(3.19e-4),Ntotal[0]/(7.98e-5),Ototal[0]/(6.39e-4)

    #calculate the surface gravity
    Rsquared=(10**L)*Lsun/(4*math.pi*sigma*(10**Teff)**4)
    R = np.sqrt(Rsquared)/Rsun
    g = M*Msun*Grav/Rsquared
    logg = np.log10(g)



    startH=Hydrogen[0]
    Hestart=Hetotalnorm[0]
    Cstart=Ctotalnorm[0]
    Nstart=Ntotalnorm[0]
    Ostart =Ototalnorm[0]

    #plot the tracks and the grid points
    pylab.plot(Teff,L, color='grey', linewidth=2)
    for jj in gridpoints:
        #print input paramters
        #print massarr[imass],jj,M[jj-1],Teff[jj-1],L[jj-1],R[jj-1],logg[jj-1]
        pylab.plot(Teff[jj-1],L[jj-1], 's',color='black', markersize=7)
        


        



        
        directory=modelloc+str(model+1)
        if not os.path.exists(directory):
                os.makedirs(directory)
        #This opens each file
        file=open(modelloc+str(model+1)+'/in.awa', 'a')

        Teffmodel=Teff[jj-1]
        loggmodel=logg[jj-1]
        Rmodel=R[jj-1]
        
        


        #these are for 2 solar metalicity
        #k=[.279,.273,.358,.349,.340,.089,.042,.134,.266,.260,.257,.339,.331,.308,.248,.175,.249,.244,.243,.241,.319,.309,.297,.071,.228,.223,.223,.223,.222,.219,.290,.120,.214,.210,.210,.209,.207,.277,.126,.081,.199,.195,.195,.195,.194,.191,.136,.172,.069,.068,.077,.176,.175,.093,.146,.145,.048,.047,.052,.056,.062,.063,.066,.070,.154,.030,.030,.031,.035,.039,.043,.045,.169,.016,.015,.017,.018,.020,.020,.020,.024,.027,.031,.015,.012,2.415]
        #alpha=[.620,.620,.620,.619,.619,.639,.647,.642,.620,.620,.620,.619,.619,.619,.646,.653,.620,.620,.620,.619,.619,.619,.620,.695,.620,.620,.620,.620,.619,.619,.619,.625,.620,.620,.620,.619,.619,.619,.625,.682,.620,.620,.620,.619,.619,.619,.625,.665,.620,.620,.620,.619,.619,.625,.625,.464,.620,.620,.620,.619,.619,.619,.625,.625,.625,.620,.620,.620,.620,.619,.625,.625,.625,.620,.620,.620,.620,.625,.625,.625,.625,.625,.611,.625,.625,.431]
        #delta=[.05,.05,.05,.05,.05,.075,.05,.075,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.075,.075,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.070,.075,.05,.05,.05,.05,.05,.05,.05,.07,.07,.075,.05,.05,.05,.05,.05,.07,.07,.075,.05,.05,.05,.05,.07,.07,.07,.07,.07,.05,.07,.07,.05]
    
        k = LFParameters.kdefine(Teffmodel, loggmodel)
        alpha = LFParameters.alphadefine(Teffmodel, loggmodel)
        delta = LFParameters.deltadefine(Teffmodel, loggmodel)


        #Z is in units of Z/Zsun, where Zsun is 0.02
        Z=.7
    
    
        #Defining the abundances
        H=1.0
    
    
        HE=(Hestart  /.1)
        
    
        LE=.94*Z
        BE=.9592*Z
        B=1.43*Z
    
    
        C=(Cstart /3.19e-4)
        N=(Nstart  /7.98e-5)
        O=(Ostart  /6.39e-4)
        print C, N, O
    
        F=1.008*Z
        NE=.709*Z
        NA=.823*Z
        MG=1.047*Z
        AL=.9366*Z
        SI=.9288*Z
        P=.927*Z
        S=.623*Z
        CL=.987*Z
        AR=1.004*Z
        K=.823*Z
        CA=.947*Z
        SC=.94*Z
        TI=.891*Z
        V=.851*Z
        CR=.928*Z
        MN=1.076*Z
        FE=.9875*Z
        CO=1.136*Z
        NI=.92*Z
        CU=.911*Z
        ZN=.9075*Z
    
    
    



        ABUNDOPT = '2\n'
        ABUNDL1=str(H)+','+str(HE)+','+str(LE)+','+str(BE)+','+str(B)+','+str(C)+','+str(N)+','+str(O)+','+str(F)+','+str(NE)+',\n'
        ABUNDL2=str(NA)+','+str(MG)+','+str(AL)+','+str(SI)+','+str(P)+','+str(S)+','+str(CL)+','+str(AR)+','+str(K)+','+str(CA)+',\n'
        ABUNDL3=str(SC)+','+str(TI)+','+str(V)+','+str(CR)+','+str(MN)+','+str(FE)+','+str(CO)+','+str(NI)+','+str(CU)+','+str(ZN)+',\n'
        PARAM_BASIC=str(10**Teffmodel)+','+str(loggmodel)+','+str(Rmodel)+'\n'
        HYDROL1="""       0.  , 100.,   'OBR'     , 10.  ,   F ,'***'\n"""
        HYDROL2="""            "'NO'"      "'TN'"      "'YE'"\n """
        STARTVAL=str(k)+','+str(alpha)+','+str(delta)+'\n'
        CRAY = 'F\n'
        BLOCKING = '    0.1,  0.1,  500.\n'
        SYNTHSPEC=' 1.e-50, 0.01, 5000.\n'
        FRANGEL1='     200.     ,     1150.   ,    0.5\n'
        FRANGEL2='    1150.     ,     2124.   ,    1.0\n'
        TURBVEL='     0.10    ,     10.    ,    1\n'
    
    
    
    
        #This is the block of text that is appended to each file
        #Namelists
        NAMEL1='&*\n'
        NAMEL2="&BASICPARAM\n"
        NAMEL3=" OSHOCK= ,OSHOCK2= ,OAUGER = ,OPTFM  = ,OPTNEB = ,OPTELEM= ,NTZ    = ,\n"
        NAMEL4=" OPTBL1= ,OPTSELF= ,NFLUXM = ,OPTSPEC= ,OPTLB2 = ,OPTBADD= ,NOPTBM = ,\n"
        NAMEL5=" OPTLB3= ,OPTUPQ0= ,OPTHOPF= ,ITEMP  = ,OPTTHCO= ,TLOW   = ,IONISSC= ,\n"
        NAMEL6="/\n"
        NAMEL7="&ENHIBLOCK\n"
        NAMEL8=" WAVBLUE= ,WAVRED = ,DLAM    = ,VMICRO  = ,ATURB = ,TAUUL  = ,\n"
        NAMEL9=" NSAMP  = ,ITBLOCK= ,ITB1    = ,ITB3    = ,\n"
        NAMEL10=" RANGE  = ,TJCH   = ,TAU0B   = ,TAU0KB  = ,TAUKB = ,\n"
        NAMEL11=" OPTUL  = ,OULTLA = ,OPTSHIFT= ,OPTVOIGT= ,OPTLUM= ,OPTNEGH= ,OPTCORR= ,\n"
        NAMEL12="/\n"
        NAMEL13="&ENHINPS\n"
        NAMEL14=" TURBVR= ,XLBOLL= ,BETAS= ,VMINM= ,\n"
        NAMEL15="/\n"
        NAMEL16="&*\n"
        NAMEL17="&ENHINEB\n"
        NAMEL18=" RNEB= \n,"
        NAMEL19="/\n"
        NAMEL20="&ENHISPE\n"
        NAMEL21=" QINFH= ,Q0H    = ,GAMH   = ,FLUXCT= ,ACC = ,\n"
        NAMEL22=" WAV1 = ,WAV2   = ,WAV3   = ,TRM1  = ,TRM2= ,TRM3= ,\n"
        NAMEL23=" MODEL= ,MODSCAL= ,MODSCKM= ,\n"
        NAMEL24=" ICALC= , , , , , , , , ,\n"
        NAMEL25="/\n"
        NAMEL26="&MODPARAM\n"
        NAMEL27=" OPTSH1 = ,OPTSH2 = ,OPTALD= ,OPTPHO = ,OPTCOL = ,\n"
        NAMEL28=" OPTDR  = ,OPTSOUT= ,OPTSIN= ,OPTABU = ,OPTDIL = ,OPTDEP= ,\n"
        NAMEL29=" OPTLTE = ,OPTDIFF= ,OPTALI= ,OPTALEX= ,OPTINT = ,OPTEXL= ,\n"
        NAMEL30=" OPTHOUT= ,OPTOUT = ,OPTNL = ,OPTCONT= ,OPTJSIN= ,TAUDUM= ,\n"
        NAMEL31="/\n"
        NAMEL32="&:\n"
    


        file.write(ABUNDOPT)
        file.write(ABUNDL1)
        file.write(ABUNDL2)
        file.write(ABUNDL3)
        file.write(PARAM_BASIC)
        file.write(HYDROL1)
        file.write(HYDROL2)
        file.write(STARTVAL)
        file.write(CRAY)
        file.write(BLOCKING)
        file.write(SYNTHSPEC)
        file.write(FRANGEL1)
        file.write(FRANGEL2)
        file.write(TURBVEL)
    

        #This is where the lines are added to each file
        file.write(NAMEL1)
        file.write(NAMEL2)
        file.write(NAMEL3)
        file.write(NAMEL4)
        file.write(NAMEL5)
        file.write(NAMEL6)
        file.write(NAMEL7)
        file.write(NAMEL8)
        file.write(NAMEL9)
        file.write(NAMEL10)
        file.write(NAMEL11)
        file.write(NAMEL12)
        file.write(NAMEL13)
        file.write(NAMEL14)
        file.write(NAMEL15)
        file.write(NAMEL16)
        file.write(NAMEL17)
        file.write(NAMEL18)
        file.write(NAMEL19)
        file.write(NAMEL20)
        file.write(NAMEL21)
        file.write(NAMEL22)
        file.write(NAMEL23)
        file.write(NAMEL24)
        file.write(NAMEL25)
        file.write(NAMEL26)    
        file.write(NAMEL27)
        file.write(NAMEL28)
        file.write(NAMEL29)
        file.write(NAMEL30)
        file.write(NAMEL31)
        file.write(NAMEL32)
        model+=1
    

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

