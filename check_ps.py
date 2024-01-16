import numpy as np
import matplotlib.pyplot as plt

Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1
#=========functions==============#
def error(PS,NN):
    '''calculate sigma in chi2'''
    errors=np.zeros(1000)
    for i in np.arange(2,1002,1):
        errors[i-2]=((PS[i-2]+NN[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
    #print(errors)
    return errors

#=========noise ps============#
spectrum=np.zeros(1000)
for i in np.arange(2,1002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

data1=np.loadtxt('reio_camb00_cl_lensed.dat')
data2=np.loadtxt('reio_mine00_cl_lensed.dat')

l1=data1[:,0]
l2=data2[:,0]
EE1=data1[:,1]
EE2=data2[:,1]

errors_EE=error(EE2,spectrum)
plt.loglog(l2[0:1000],EE2[0:1000],label="reio_mine")
plt.loglog(l1[0:1000],EE1[0:1000],label="reio_camb")
plt.legend()
#plt.errorbar(np.arange(2,1002,1),EE2[0:1000],yerr=errors_EE)
plt.savefig("check_EE.jpg")