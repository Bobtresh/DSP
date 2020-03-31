from math import *
#import matplotlib
#matplotlib.use('qt4agg')
import matplotlib.pyplot as plt
from scipy import *
from scipy import signal
from scipy import fftpack
import scipy.io.wavfile as wav
import numpy as np
import scipy.io as mat


data = mat.loadmat("Dataset_1.mat")['H']
c = 299792458;#m/s

def channel2APDP (fmeting):

    #fmeting is 2d array (100 metingen op 1 pos)
    
    #print(np.shape(fmeting))
    
    #PDP opstellen
    PDP=0
    for i in range(0,100):
        PDP += fftpack.ifft(fmeting[:,i]*signal.gaussian(201, 50))
    

    PDP = PDP/100
    APDP = abs(PDP) ** 2
    plt.plot(range(201),APDP)
    plt.show()
    return APDP
    
def APDP2delays(ADPD):
    tau = signal.argrelextrema(ADPD, np.greater)
    return tau
    



for k in range(24):
    APDP = channel2APDP(data[:,k,:])#Meting eerste positie
    tau = APDP2delays(APDP)
    print(tau)
    