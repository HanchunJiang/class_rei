import numpy as np

#l：1-2500
#CMB temparature: muK
Tcmb=2.75*10**3
#sensitivity of each channel: muK-arcmin
sigma_nu0=[37.42,33.46,21.31,16.87,12.07,11.30,10.34,7.69,7.25,5.57,7.05,10.79,13.80,21.95,47.45]
#sensitivity of each channel: muK-rad
sigma_nu=[i*np.pi/180/60 for i in sigma_nu0]

#beam size: arcmin
theta_nu0=[70.5,58.5,51.1,41.6,36.9,33.0,30.2,26.3,23.7,28.9,28.0,24.7,22.5,20.9,17.9]
#beam size: rad
theta_nu=[i*np.pi/180/60 for i in theta_nu0]

spectrum=np.zeros(800)
for i in np.arange(2,802,1):
    sum=0
    for j in range(len(sigma_nu)):
        sum+=1.0/((sigma_nu[j]/Tcmb)**2*np.exp(i*(i+1)*theta_nu[j]/8/np.log(2)))
    spectrum[i-2]=1.0/sum
np.save("spectrum.npy",spectrum)
