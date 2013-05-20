
import os

for model in range(85):
	directory=str(model+1)
	if not os.path.exists(directory):
    		os.makedirs(directory)
	#This opens each file
	file=open(str(model+1)+'/in.awa', 'a')





	#Defining key variables
	Teff=[59870, 52061, 49139, 46967, 46330, 25085, 22339, 25100, 58567, 50928, 48499, 46122, 43501, 35514, 31527, 33117,57000, 49566, 47765, 45683, 42474, 38434, 36653, 24041, 54635, 47509, 46277, 44963, 43138, 40319, 34971,25314, 52465, 45622, 43576, 40507, 37807, 33037, 24880, 29759, 50294, 43734, 42084, 40205, 36500, 32858,26494, 32953, 45971, 39975, 37688, 34549, 32589, 29727, 24838, 15267, 43811, 38097, 36525, 35524, 34052,32982, 29531, 26636, 23768, 40422, 35150, 34298, 33160, 31151, 29320, 27925, 24035, 35864, 31186, 30294,30016, 29660, 29253, 28766, 26393, 24266, 22909, 25453]
	logg=[4.322, 4.078, 3.954, 3.836, 3.761, 2.622, 2.434, 3.017, 4.323, 4.081, 3.972, 3.850, 3.700, 3.277, 3.014, 3.235, 4.352,4.108, 4.016, 3.907, 3.749, 3.512, 3.350, 2.468, 4.383, 4.139, 4.070, 3.985, 3.884, 3.722, 3.428, 2.784,4.393, 4.150, 4.014, 3.824, 3.673, 3.386, 2.817, 2.917, 4.412, 4.170, 4.058, 3.920, 3.678, 3.451, 3.024, 3.122,4.402, 4.159, 3.966, 3.723, 3.584, 3.385, 3.020, 1.872, 4.439, 4.196, 4.056, 3.954, 3.833, 3.744, 3.493,3.266, 3.029, 4.452, 4.209, 4.124, 3.999, 3.804, 3.644, 3.525, 3.195, 4.469, 4.226, 4.113, 4.067, 4.014, 3.969,3.910, 3.665, 3.456, 3.313, 4.237]

	R=[12.4, 16.3, 18.4, 20.1, 20.6, 68.7, 59.2, 15.4, 11.3, 14.9, 16.7, 18.6, 21.1, 31.7, 36.9, 14.3, 9.8, 12.9, 14.2, 15.9, 18.8, 23.2, 26.2, 58.4, 8.2, 10.8, 11.7, 12.8, 14.3, 16.8, 23.0, 45.1, 7.4, 9.7, 11.3, 13.9, 16.4, 22.1, 40.4, 23.5, 6.5, 8.5, 9.7, 11.2, 14.5, 18.5, 29.6, 17.9, 5.7, 7.5, 9.3, 12.0, 14.0, 17.5, 26.1, 75.4, 5.0, 6.5, 7.7, 8.5, 9.8, 10.7, 14.3, 18.2, 23.7, 4.4, 5.7, 6.3, 7.3, 9.0, 10.8, 12.3, 17.9, 3.7, 4.9, 5.6, 5.9, 6.2,6.6, 7.0, 9.3, 11.7, 13.7, 3.9]

	#these are for .2 solar metalicity
	#k=[.179,.176,.219,.210,.199,.069,.034,.116,.175,.173,.169,.210,.201,.182,.158,.124,.172,.170,.167,.163,.205,.193,.179,.042,.167,.165,.163,.161,.158,.154,.191,.080,.164,.162,.159,.154,.151,.190,.086,.058,.160,.158,.155,.152,.147,.143,.094,.107,.069,.068,.074,.144,.141,.072,.105,.180,.053,.052,.055,.058,.060,.062,.056,.058,.113,.038,.037,.039,.041,.045,.040,.041,.126,.023,.023,.025,.025,.022,.023,.023,.026,.028,.033,.020,.016,6.048]
	#alpha=[.535,.534,.534,.534,.533,.549,.556,.552,.535,.534,.534,.534,.533,.532,.543,.552,.535,.534,.534,.534,.534,.533,.532,.605,.535,.534,.534,.534,.534,.534,.533,.558,.535,.534,.534,.534,.534,.533,.558,.583,.535,.534,.534,.534,.533,.533,.558,.570,.535,.534,.534,.534,.533,.556,.558,.350,.535,.535,.534,.534,.534,.534,.556,.556,.558,.535,.535,.534,.534,.534,.556,.556,.559,.535,.535,.534,.534,.557,.557,.556,.556,.556,.538,.557,.557,.328]
	#delta=[.05,.05,.05,.05,.05,.075,.05,.075,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.075,.075,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.070,.075,.05,.05,.05,.05,.05,.05,.05,.07,.07,.075,.05,.05,.05,.05,.05,.07,.07,.075,.05,.05,.05,.05,.07,.07,.07,.07,.07,.05,.07,.07,.05]


	#these are for 2 solar metalicity
	k=[.279,.273,.358,.349,.340,.089,.042,.134,.266,.260,.257,.339,.331,.308,.248,.175,.249,.244,.243,.241,.319,.309,.297,.071,.228,.223,.223,.223,.222,.219,.290,.120,.214,.210,.210,.209,.207,.277,.126,.081,.199,.195,.195,.195,.194,.191,.136,.172,.069,.068,.077,.176,.175,.093,.146,.145,.048,.047,.052,.056,.062,.063,.066,.070,.154,.030,.030,.031,.035,.039,.043,.045,.169,.016,.015,.017,.018,.020,.020,.020,.024,.027,.031,.015,.012,2.415]
	alpha=[.620,.620,.620,.619,.619,.639,.647,.642,.620,.620,.620,.619,.619,.619,.646,.653,.620,.620,.620,.619,.619,.619,.620,.695,.620,.620,.620,.620,.619,.619,.619,.625,.620,.620,.620,.619,.619,.619,.625,.682,.620,.620,.620,.619,.619,.619,.625,.665,.620,.620,.620,.619,.619,.625,.625,.464,.620,.620,.620,.619,.619,.619,.625,.625,.625,.620,.620,.620,.620,.619,.625,.625,.625,.620,.620,.620,.620,.625,.625,.625,.625,.625,.611,.625,.625,.431]
	delta=[.05,.05,.05,.05,.05,.075,.05,.075,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.075,.075,.05,.05,.05,.05,.05,.05,.075,.05,.05,.05,.05,.05,.05,.070,.075,.05,.05,.05,.05,.05,.05,.05,.07,.07,.075,.05,.05,.05,.05,.05,.07,.07,.075,.05,.05,.05,.05,.07,.07,.07,.07,.07,.05,.07,.07,.05]
	

	#Z is in units of Z/Zsun
	Z=2

	def HEcase(model):
		HESOLAR=0.85
		if model==4:
			return 1.1*HESOLAR
		elif model==5:
			return 1.4*HESOLAR
		elif model==6:
			return 2.2*HESOLAR
		elif model==7:
			return 3.0*HESOLAR
		elif model==8:
			return 3.2*HESOLAR
		elif model==13:
			return 2.0*HESOLAR
		elif model==14:
			return 3.0*HESOLAR
		elif model==15:
			return 3.0*HESOLAR
		elif model==16:
			return 3.0*HESOLAR
		elif model==22:
			return 1.2*HESOLAR
		elif model==23:
			return 1.7*HESOLAR
		elif model==24:
			return 3.0*HESOLAR
		elif model==32:
			return 1.1*HESOLAR
		else:
			return HESOLAR
	
	def Ccase(model):
		CSOLAR=0.815
		if model==4:
			return CSOLAR/26
		elif model==5:
			return CSOLAR/21
		elif model==6:
			return CSOLAR/18
		elif model==7:
			return CSOLAR/18
		elif model==8:
			return CSOLAR/18
		elif model==13:
			return CSOLAR/22
		elif model==14:
			return CSOLAR/18
		elif model==15:
			return CSOLAR/18
		elif model==16:
			return CSOLAR/17
		elif model==22:
			return CSOLAR/24
		elif model==23:
			return CSOLAR/20
		elif model==24:
			return CSOLAR/16
		elif model==32:
			return CSOLAR/28
		else:
			return CSOLAR
	
	def Ncase(model):
		NSOLAR=0.814
		if model==4:
			return 9*NSOLAR
		elif model==5:
			return 11*NSOLAR
		elif model==6:
			return 12*NSOLAR
		elif model==7:
			return 12*NSOLAR
		elif model==8:
			return 12*NSOLAR
		elif model==13:
			return 11*NSOLAR
		elif model==14:
			return 12*NSOLAR
		elif model==15:
			return 12*NSOLAR
		elif model==16:
			return 12*NSOLAR
		elif model==22:
			return 10*NSOLAR
		elif model==23:
			return 12*NSOLAR
		elif model==24:
			return 12*NSOLAR
		elif model==32:
			return 9*NSOLAR
		else:
			return NSOLAR
	
	def Ocase(model):
		OSOLAR=0.719
		if model==4:
			return 2*OSOLAR
		elif model==5:
			return 4*OSOLAR
		elif model==6:
			return 17*OSOLAR
		elif model==7:
			return 31*OSOLAR
		elif model==8:
			return 31*OSOLAR
		elif model==13:
			return 20*OSOLAR
		elif model==14:
			return 31*OSOLAR
		elif model==15:
			return 31*OSOLAR
		elif model==16:
			return 32*OSOLAR
		elif model==22:
			return 4*OSOLAR
		elif model==23:
			return 8*OSOLAR
		elif model==24:
			return 32*OSOLAR
		elif model==32:
			return 2*OSOLAR
		else:
			return OSOLAR
	
	
	
	
	#Defining the abundances
	H=1.0
	
	
	HE=HEcase(model)
	
	
	LE=.94*Z
	BE=.9592*Z
	B=1.43*Z
	
	
	C=Ccase(model)*Z
	N=Ncase(model)*Z
	O=Ocase(model)*Z
	
	
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
	PARAM_BASIC=str(Teff[model])+','+str(logg[model])+','+str(R[model])+'\n'
	HYDROL1="""       0.  , 100.,   'OBR'     , 10.  ,   F ,'***'\n"""
	HYDROL2="""            "'NO'"      "'TN'"      "'YE'"\n """
	STARTVAL=str(k[model])+','+str(alpha[model])+','+str(delta[model])+'\n'
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
	
